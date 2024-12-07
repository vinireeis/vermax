from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.models.accounts.account_model import AccountModel
from src.domain.models.transactions.transaction_model import TransactionModel


class IAccountsRepository(ABC):
    @abstractmethod
    async def update_balance(
        self, transaction_model: TransactionModel
    ) -> TransactionModel:
        pass

    @abstractmethod
    async def get_user_account(self, account_id: UUID) -> AccountModel:
        pass
