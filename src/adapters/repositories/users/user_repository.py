from uuid import UUID

from loguru import logger
from sqlalchemy import delete, func, select, update
from sqlalchemy.exc import IntegrityError, NoResultFound
from witch_doctor import WitchDoctor

from src.application.data_types.requests.users.user_request import (
    UpdateUserRequest,
)
from src.application.ports.repositories.users.i_user_repository import (
    IUserRepository,
)
from src.domain.exceptions.adapters.exception import (
    CpfAlreadyExistsException,
    EmailAlreadyExistsException,
    UnexpectedRepositoryException,
    UserEmailNotFoundException,
    UserNotFoundByAccountIdException,
    UserNotFoundException,
)
from src.domain.models.users.user_model import PaginatedUsersModel, UserModel
from src.externals.ports.infrastructures.i_db_config_infrastructure import (
    IDbConfigInfrastructure,
)


class UserRepository(IUserRepository):
    _postgres_sql_alchemy_infrastructure: IDbConfigInfrastructure

    @WitchDoctor.injection
    def __init__(
        self, postgres_sql_alchemy_infrastructure: IDbConfigInfrastructure
    ):
        UserRepository._postgres_sql_alchemy_infrastructure = (
            postgres_sql_alchemy_infrastructure
        )

    @classmethod
    async def insert_new_user(cls, user_model: UserModel) -> UserModel:
        async with (
            cls._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            try:
                session.add(user_model)
                await session.commit()
                await session.refresh(user_model)
                return user_model

            except IntegrityError as ex:
                logger.info(str(ex.orig))
                if bool('cpf' in ex.orig.args[0]):
                    raise CpfAlreadyExistsException()
                raise EmailAlreadyExistsException()

    @classmethod
    async def get_user_by_id(cls, user_id: int) -> UserModel:
        async with (
            cls._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            statement = select(UserModel).where(UserModel.id == user_id)
            try:
                db_result = await session.execute(statement)
                user_model = db_result.scalar_one()
                return user_model

            except NoResultFound as ex:
                logger.info(ex)
                raise UserNotFoundException(user_id)

    @classmethod
    async def get_user_by_email(cls, email: str) -> UserModel:
        async with (
            cls._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            statement = select(UserModel).where(UserModel.email == email)
            try:
                db_result = await session.execute(statement)
                user_model = db_result.scalar_one()
                return user_model

            except NoResultFound as ex:
                logger.info(ex)
                raise UserEmailNotFoundException()

    @classmethod
    async def get_user_by_account_id(cls, account_id: UUID) -> UserModel:
        async with (
            cls._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            statement = select(UserModel).where(
                UserModel.account_id == account_id
            )
            try:
                db_result = await session.execute(statement)
                user_model = db_result.scalar_one()
                return user_model

            except NoResultFound as ex:
                logger.info(ex)
                raise UserNotFoundByAccountIdException()

    @classmethod
    async def get_paginated_users(
        cls, limit: int, offset: int
    ) -> PaginatedUsersModel:
        async with (
            cls._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            try:
                statement = select(UserModel).limit(limit).offset(offset)
                db_result = await session.execute(statement)
                users_model = db_result.scalars().all()

                total_users = await session.execute(
                    select(func.count(UserModel.id))
                )
                total_count = total_users.scalar()

                return PaginatedUsersModel(
                    users=users_model,
                    total=total_count,
                    limit=limit,
                    offset=offset,
                )

            except Exception as ex:
                logger.info(ex)
                raise UnexpectedRepositoryException(original_error=ex)

    @classmethod
    async def delete_user_by_id(cls, user_id: int) -> bool:
        async with (
            cls._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            try:
                statement = (
                    delete(UserModel)
                    .where(UserModel.id == user_id)
                    .returning(UserModel.id)
                )
                db_result = await session.execute(statement)
                deleted_id = db_result.scalar()
                await session.commit()
                return bool(deleted_id)

            except Exception as ex:
                logger.info(ex)
                raise UnexpectedRepositoryException(original_error=ex)

    @classmethod
    async def update_user_by_id(
        cls, user_id: int, update_user_request: UpdateUserRequest
    ):
        async with (
            cls._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            try:
                user_data_to_update = update_user_request.model_dump()

                statement = (
                    update(UserModel)
                    .where(UserModel.id == user_id)
                    .values(**user_data_to_update)
                    .returning(UserModel)
                )
                await session.execute(statement)
                await session.commit()

            except NoResultFound as ex:
                logger.info(ex)
                raise UserNotFoundException(user_id)

            except IntegrityError as ex:
                logger.info(str(ex.orig))
                raise EmailAlreadyExistsException()
