from datetime import datetime

from src.application.data_types.dtos.jwt_dto import (
    AccessTokenDto,
    JwtDecodedDto,
    UserDataToEncodeDto,
)
from src.application.data_types.enums.token_enum import TokenTypeEnum
from src.application.ports.presenters.auth.i_jwt_presenter import IJwtPresenter
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)
from src.domain.models.users.user_model import UserModel


class JwtPresenter(IJwtPresenter):
    @staticmethod
    def from_input_form_to_data_encode_request(
        user_model: UserModel, exp: datetime
    ) -> UserDataToEncodeDto:
        try:
            jwt_typed_dict = UserDataToEncodeDto(
                user_id=user_model.id,
                account_id=user_model.account_id,
                cpf=user_model.cpf,
                email=user_model.email,
                exp=exp,
            )

            return jwt_typed_dict

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_token_decoded_raw_to_jwt_dto(
        token_decoded_raw: dict,
    ) -> JwtDecodedDto:
        try:
            jwt_dto = JwtDecodedDto(
                user_id=token_decoded_raw['user_id'],
                account_id=token_decoded_raw['account_id'],
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
