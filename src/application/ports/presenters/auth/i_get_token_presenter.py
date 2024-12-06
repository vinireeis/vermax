from abc import ABC, abstractmethod

from src.application.data_types.dtos.jwt_dto import AccessTokenDto
from src.application.data_types.requests.auth.jwt_request import (
    UserTokenDataRequest,
)
from src.application.data_types.responses.auth.token_response import (
    GetTokenResponse,
)
from src.domain.models.users.user_model import UserModel


class IGetTokenPresenter(ABC):
    @staticmethod
    @abstractmethod
    def from_input_form_to_data_encode_request(
        user_model: UserModel,
    ) -> UserTokenDataRequest:
        pass

    @staticmethod
    @abstractmethod
    def from_access_token_dto_to_output_response(
        access_token_dto: AccessTokenDto,
    ) -> GetTokenResponse:
        pass
