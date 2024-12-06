from abc import ABC

from fastapi.security import OAuth2PasswordRequestForm

from src.application.data_types.dtos.jwt_dto import AccessTokenDto


class IGetTokenUseCase(ABC):
    @classmethod
    async def get_token(
        cls, form_data: OAuth2PasswordRequestForm
    ) -> AccessTokenDto:
        pass
