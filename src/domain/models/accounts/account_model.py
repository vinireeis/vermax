import uuid

from sqlalchemy import UUID, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.models.orm.base_model import Base


class AccountModel(Base):
    __tablename__ = 'accounts'

    account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    balance: Mapped[int] = mapped_column(Integer, default=0)
    branch_id: Mapped[int] = mapped_column(
        String(4), nullable=False, default='0001'
    )

    user: Mapped['User'] = relationship(  # noqa: F821
        argument='User', back_populates='account'
    )
