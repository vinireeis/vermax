from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from src.application.data_types.responses.api.base_response import (
    BaseApiResponse,
)


class TransferPayload(BaseModel):
    transaction_id: UUID
    account_id: UUID
    amount: Decimal
    operation: str
    created_at: Optional[datetime]


class TransferCashResponse(BaseApiResponse):
    payload: TransferPayload
