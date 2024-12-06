from src.application.data_types.dtos.user_dto import PaginatedUsersDto, UserDto
from src.application.data_types.responses.users.user_response import (
    GetPaginatedUsersResponse,
    GetUserResponse,
    PaginatedUsersPayload,
    UserPayload,
)
from src.application.ports.presenters.users.i_get_users_presenter import (
    IGetUsersPresenter,
)
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)
from src.domain.models.users.user_model import PaginatedUsersModel, UserModel


class GetUsersPresenter(IGetUsersPresenter):
    @staticmethod
    def from_model_to_dto(model: UserModel) -> UserDto:
        try:
            user_dto = UserDto(
                id=model.id,
                name=model.name,
                email=model.email,
                cpf=model.cpf,
                account_id=model.account_id,
            )

            return user_dto

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_paginated_model_to_dto(
        model: PaginatedUsersModel,
    ) -> PaginatedUsersDto:
        try:
            users_dto = [
                UserDto(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    cpf=user.cpf,
                    account_id=user.account_id,
                )
                for user in model.users
            ]

            paginated_users_dto = PaginatedUsersDto(
                total=model.total,
                users=users_dto,
                limit=model.limit,
                offset=model.offset,
            )

            return paginated_users_dto

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_dto_to_output_response(user_dto: UserDto) -> GetUserResponse:
        try:
            user_payload = UserPayload(
                name=user_dto.name,
                email=user_dto.email,
                cpf=user_dto.cpf,
                account_id=user_dto.account_id,
                id=user_dto.id,
            )
            get_user_response = GetUserResponse(
                payload=user_payload, success=True
            )
            return get_user_response

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_paginated_dto_to_output_response(
        paginated_users_dto: PaginatedUsersDto,
    ) -> GetPaginatedUsersResponse:
        try:
            users_payload = [
                UserPayload(
                    name=user.name,
                    email=user.email,
                    cpf=user.cpf,
                    account_id=user.account_id,
                    id=user.id,
                )
                for user in paginated_users_dto.users
            ]
            paginated_users_payload = PaginatedUsersPayload(
                users=users_payload,
                total=paginated_users_dto.total,
                limit=paginated_users_dto.limit,
                offset=paginated_users_dto.offset,
            )

            get_paginated_user_response = GetPaginatedUsersResponse(
                payload=paginated_users_payload, success=True
            )

            return get_paginated_user_response

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)
