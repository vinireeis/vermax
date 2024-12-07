import uuid
from datetime import datetime
from decimal import Decimal

from sqlalchemy import DECIMAL, UUID, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.models.orm.base_model import Base


class AccountModel(Base):
    __tablename__ = 'accounts'

    account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    balance: Mapped[Decimal] = mapped_column(
        DECIMAL(precision=10, scale=2), default=Decimal('0.00')
    )
    branch_id: Mapped[str] = mapped_column(
        String(4), nullable=False, default='0001'
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(), onupdate=datetime.now()
    )

    user: Mapped['UserModel'] = relationship(  # noqa: F821
        argument='UserModel',
        back_populates='account',
        uselist=False,
    )
    transactions: Mapped[list['TransactionModel']] = relationship(  # noqa: F821
        argument='TransactionModel', back_populates='account'
    )
