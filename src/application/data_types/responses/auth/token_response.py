from pydantic import BaseModel


class GetTokenResponse(BaseModel):
    access_token: str
    token_type: str
