from datetime import datetime

from pydantic import BaseModel


class UserTokenDataRequest(BaseModel):
    account_id: str
    cpf: str
    email: str
    exp: datetime
    user_id: int
