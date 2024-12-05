from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True, frozen=True)
class UserDto:
    id: int
    name: str
    email: str
    cpf: str
    account_id: UUID


@dataclass(slots=True, frozen=True)
class PaginatedUsersDto:
    users: list[UserDto]
    total: int
    limit: int
    offset: int
