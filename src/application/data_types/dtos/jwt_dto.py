from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True, frozen=True)
class JwtDecodedDto:
    account_id: UUID
    cpf: str
    email: str
    user_id: int


@dataclass(slots=True, frozen=True)
class AccessTokenDto:
    access_token: str
    token_type: str
