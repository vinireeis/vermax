from abc import ABC, abstractmethod

from src.domain.models.transactions.transaction_model import TransactionModel


class IAccountsRepository(ABC):
    @classmethod
    @abstractmethod
    async def update_balance(
        cls, transaction_model: TransactionModel
    ) -> TransactionModel:
        pass
