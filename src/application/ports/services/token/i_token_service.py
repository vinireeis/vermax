from abc import ABC, abstractmethod

from src.application.data_types.dtos.jwt_dto import (
    AccessTokenDto,
    JwtDecodedDto,
)
from src.application.data_types.requests.auth.jwt_request import (
    UserTokenDataRequest,
)


class ITokenService(ABC):
    @classmethod
    @abstractmethod
    async def generate_token(
        cls, user_token_data_request: UserTokenDataRequest
    ) -> AccessTokenDto:
        pass

    @classmethod
    @abstractmethod
    async def validate_token(cls, jwt: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    async def decode_token(cls, jwt: str) -> JwtDecodedDto:
        pass
