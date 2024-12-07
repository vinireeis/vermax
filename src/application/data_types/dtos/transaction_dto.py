from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Literal
from uuid import UUID

from src.domain.models.transactions.enums.transactions_enum import (
    TransactionOperationEnum,
)


@dataclass(slots=True, frozen=True)
class TransactionDto:
    transaction_id: UUID
    account_id: UUID
    amount: Decimal
    operation: Literal[TransactionOperationEnum.TRANSFER]
    created_at: datetime = None
