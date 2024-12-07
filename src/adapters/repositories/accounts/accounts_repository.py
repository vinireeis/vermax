from uuid import UUID

from loguru import logger
from sqlalchemy import select
from witch_doctor import WitchDoctor

from src.application.ports.repositories.accounts.accounts_repository import (
    IAccountsRepository,
)
from src.domain.exceptions.adapters.exception import (
    UnexpectedRepositoryException,
)
from src.domain.models.accounts.account_model import AccountModel
from src.domain.models.transactions.transaction_model import TransactionModel
from src.externals.ports.infrastructures.i_db_config_infrastructure import (
    IDbConfigInfrastructure,
)


class AccountsRepository(IAccountsRepository):
    _postgres_sql_alchemy_infrastructure: IDbConfigInfrastructure

    @WitchDoctor.injection
    def __init__(
        self, postgres_sql_alchemy_infrastructure: IDbConfigInfrastructure
    ):
        self._postgres_sql_alchemy_infrastructure = (
            postgres_sql_alchemy_infrastructure
        )

    async def get_user_account(self, account_id: UUID) -> AccountModel:
        async with (
            self._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            try:
                statement = select(AccountModel).filter_by(
                    account_id=account_id
                )
                result_db = await session.execute(statement)
                account = result_db.scalar_one()
                return account

            except Exception as ex:
                logger.info(ex)
                raise UnexpectedRepositoryException(original_error=ex)

    async def update_balance(self, transaction_model: TransactionModel):
        async with (
            self._postgres_sql_alchemy_infrastructure.get_session() as session
        ):
            try:
                async with session.begin():
                    statement = (
                        select(AccountModel)
                        .filter_by(account_id=transaction_model.account_id)
                        .with_for_update()
                    )
                    result_db = await session.execute(statement)
                    account = result_db.scalar_one()

                    account.balance += transaction_model.amount
                    session.add(transaction_model)

            except Exception as ex:
                logger.info(ex)
                raise UnexpectedRepositoryException(original_error=ex)
