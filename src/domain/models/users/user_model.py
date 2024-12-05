import uuid
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import UUID, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.domain.models.orm.base_model import Base


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False
    )
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(), onupdate=datetime.now()
    )

    account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey('accounts.account_id'), nullable=False
    )
    account: Mapped['AccountModel'] = relationship(  # noqa: F821
        argument='AccountModel',
        back_populates='user',
        uselist=False,
        cascade='all, delete',
    )


@dataclass(slots=True, frozen=True)
class PaginatedUsersModel:
    users: list[UserModel]
    total: int
    limit: int
    offset: int
