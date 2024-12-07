from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID


@dataclass(slots=True, frozen=True)
class AccountDto:
    account_id: UUID
    balance: Decimal
    branch_id: str
