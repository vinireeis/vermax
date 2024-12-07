from decimal import Decimal
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field

from src.application.data_types.requests.validators.cpf_validator import (
    CpfValidatorMixin,
)
from src.domain.models.transactions.enums.transactions_enum import (
    TransactionOperationEnum,
)


class TargetAccountRequest(BaseModel):
    bank: str
    branch: str
    account_id: UUID


class OriginAccountRequest(CpfValidatorMixin, BaseModel):
    bank: str
    branch: str


class TransferCashRequest(BaseModel):
    operation: Literal[TransactionOperationEnum.TRANSFER]
    amount: Decimal = Field(ge=0.01, decimal_places=2)
    target: TargetAccountRequest
    origin: OriginAccountRequest
