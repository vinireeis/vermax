from datetime import datetime, timedelta, timezone

from decouple import config

from src.application.data_types.dtos.jwt_dto import AccessTokenDto
from src.application.data_types.requests.auth.jwt_request import (
    UserTokenDataRequest,
)
from src.application.data_types.responses.auth.token_response import (
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
            exp = datetime.now(tz=timezone.utc) + timedelta(
                minutes=int(config('JWT_TTL'))
            )

            user_token_data_request = UserTokenDataRequest(
                user_id=user_model.id,
                account_id=str(user_model.account_id),
                cpf=user_model.cpf,
                email=user_model.email,
                exp=exp,
            )

            return user_token_data_request

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_access_token_dto_to_output_response(
        access_token_dto: AccessTokenDto,
    ) -> GetTokenResponse:
        try:
            response = GetTokenResponse(
                access_token=access_token_dto.access_token,
                token_type=access_token_dto.token_type,
            )

            return response

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)
