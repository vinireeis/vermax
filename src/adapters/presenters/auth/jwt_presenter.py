from uuid import UUID

from src.application.data_types.dtos.jwt_dto import (
    AccessTokenDto,
    JwtDecodedDto,
)
from src.application.data_types.enums.token_enum import TokenTypeEnum
from src.application.ports.presenters.auth.i_jwt_presenter import IJwtPresenter
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)


class JwtPresenter(IJwtPresenter):
    @staticmethod
    def from_token_decoded_raw_to_jwt_dto(
        token_decoded_raw: dict,
    ) -> JwtDecodedDto:
        try:
            jwt_dto = JwtDecodedDto(
                user_id=token_decoded_raw['user_id'],
                account_id=UUID(token_decoded_raw['account_id']),
                cpf=token_decoded_raw['cpf'],
                email=token_decoded_raw['email'],
            )
            return jwt_dto

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def create_output_access_token(access_token: str):
        bearer_token_payload = AccessTokenDto(
            access_token=access_token, token_type=TokenTypeEnum.BEARER
        )

        return bearer_token_payload
