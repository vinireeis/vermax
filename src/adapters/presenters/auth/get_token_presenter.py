from datetime import datetime, timedelta

from decouple import config

from src.application.data_types.dtos.jwt_dto import AccessTokenDto
from src.application.data_types.requests.auth.jwt_request import (
    UserTokenDataRequest,
)
from src.application.data_types.responses.auth.token_response import (
    AccessTokenPayload,
    GetTokenResponse,
)
from src.application.ports.presenters.auth.i_get_token_presenter import (
    IGetTokenPresenter,
)
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)
from src.domain.models.users.user_model import UserModel


class GetTokenPresenter(IGetTokenPresenter):
    @staticmethod
    def from_input_form_to_data_encode_request(
        user_model: UserModel,
    ) -> UserTokenDataRequest:
        try:
            user_token_data_request = UserTokenDataRequest(
                user_id=user_model.id,
                account_id=user_model.account_id,
                cpf=user_model.cpf,
                email=user_model.email,
                exp=(datetime.now() + timedelta(minutes=config('JWT_TTL'))),
            )

            return user_token_data_request

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_access_token_dto_to_output_response(
        access_token_dto: AccessTokenDto,
    ) -> GetTokenResponse:
        try:
            access_token_payload = AccessTokenPayload(
                access_token=access_token_dto.access_token,
                token_type=access_token_dto.token_type,
            )
            response = GetTokenResponse(
                payload=access_token_payload, success=True
            )

            return response

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)
