import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import UUID, Enum, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.models.orm.base_model import Base
from src.domain.models.transactions.enums.transactions_enum import (
    TransactionOperationEnum,
)


class TransactionModel(Base):
    __tablename__ = 'transactions'

    transaction_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    amount: Mapped[Decimal] = mapped_column(
        Numeric(precision=10, scale=2), nullable=False
    )
    transaction_operation: Mapped[str] = mapped_column(
        Enum(TransactionOperationEnum), nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(), onupdate=datetime.now()
    )

    account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('accounts.account_id'), nullable=False
    )
    account: Mapped['AccountModel'] = relationship(  # noqa: F821
        argument='AccountModel', back_populates='transactions'
    )
