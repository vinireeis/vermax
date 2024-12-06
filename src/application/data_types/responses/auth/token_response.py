from pydantic import BaseModel

from src.application.data_types.responses.api.base_response import (
    BaseApiResponse,
)


class AccessTokenPayload(BaseModel):
    access_token: str
    token_type: str


class GetTokenResponse(BaseApiResponse):
    payload: AccessTokenPayload
