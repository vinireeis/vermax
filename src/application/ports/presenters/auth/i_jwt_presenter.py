from abc import ABC, abstractmethod

from src.application.data_types.dtos.jwt_dto import (
    AccessTokenDto,
    JwtDecodedDto,
)


class IJwtPresenter(ABC):
    @staticmethod
    @abstractmethod
    def from_token_decoded_raw_to_jwt_dto(
        token_decoded_raw: dict,
    ) -> JwtDecodedDto:
        pass

    @staticmethod
    @abstractmethod
    def create_output_access_token(access_token: str) -> AccessTokenDto:
        pass
