from decimal import Decimal
from uuid import UUID, uuid4

from src.domain.models.transactions.enums.transactions_enum import (
    TransactionOperationEnum,
)


class TransactionEntity:
    def __init__(
        self,
        transaction_operation: TransactionOperationEnum,
        amount: Decimal,
        account_id: UUID = None,
        transaction_id: UUID = None,
    ):
        self._transaction_id = transaction_id
        self._amount = amount
        self._transaction_operation = transaction_operation
        self._account_id = account_id

    @property
    def account_id(self) -> UUID:
        return self._account_id

    @property
    def transaction_id(self) -> UUID:
        return (
            self._transaction_id
            if self._transaction_id
            else self._generate_uuid()
        )

    @property
    def amount(self) -> Decimal:
        return self._amount

    @property
    def transaction_operation(self) -> TransactionOperationEnum:
        return self._transaction_operation

    @staticmethod
    def _generate_uuid() -> UUID:
        _id = uuid4()
        return _id
