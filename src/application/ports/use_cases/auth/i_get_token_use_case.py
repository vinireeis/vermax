from abc import ABC, abstractmethod

from fastapi.security import OAuth2PasswordRequestForm

from src.application.data_types.dtos.jwt_dto import AccessTokenDto


class IGetTokenUseCase(ABC):
    @abstractmethod
    async def get_token(
        self, form_data: OAuth2PasswordRequestForm
    ) -> AccessTokenDto:
        pass
