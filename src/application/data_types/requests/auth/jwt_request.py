from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserTokenDataRequest(BaseModel):
    account_id: UUID
    cpf: str
    email: str
    exp: datetime
    user_id: int
