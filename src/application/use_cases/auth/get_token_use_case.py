from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger
from witch_doctor import WitchDoctor

from src.application.data_types.dtos.jwt_dto import AccessTokenDto
from src.application.ports.presenters.auth.i_get_token_presenter import (
    IGetTokenPresenter,
)
from src.application.ports.presenters.users.i_user_presenter import (
    IUserPresenter,
)
from src.application.ports.repositories.users.i_user_repository import (
    IUserRepository,
)
from src.application.ports.services.token.i_token_service import ITokenService
from src.application.ports.use_cases.auth.i_get_token_use_case import (
    IGetTokenUseCase,
)
from src.domain.exceptions.application.exception import (
    UnexpectedApplicationException,
)
from src.domain.exceptions.base.exception import (
    AdapterException,
    ApplicationException,
    DomainException,
    ExternalException,
)


class GetTokenUseCase(IGetTokenUseCase):
    _user_repository: IUserRepository
    _jwt_token_service: ITokenService
    _get_token_presenter: IGetTokenPresenter
    _user_presenter: IUserPresenter

    @WitchDoctor.injection
    def __init__(
        self,
        user_repository: IUserRepository,
        jwt_token_service: ITokenService,
        get_token_presenter: IGetTokenPresenter,
        user_presenter: IUserPresenter,
    ):
        GetTokenUseCase._user_repository = user_repository
        GetTokenUseCase._jwt_token_service = jwt_token_service
        GetTokenUseCase._get_token_presenter = get_token_presenter
        GetTokenUseCase._user_presenter = user_presenter

    async def get_token(
        self, form_data: OAuth2PasswordRequestForm
    ) -> AccessTokenDto:
        try:
            user_model = await self._user_repository.get_user_by_email(
                email=form_data.username
            )
            user_entity = self._user_presenter.from_model_to_entity(
                user_model=user_model, password=form_data.password
            )

            user_entity.validate_password()

            user_token_data_request = self._get_token_presenter.from_input_form_to_data_encode_request(  # noqa: E501
                user_model=user_model
            )
            access_token_dto = await self._jwt_token_service.generate_token(
                user_token_data_request=user_token_data_request
            )
            return access_token_dto

        except (
            AdapterException,
            DomainException,
            ExternalException,
            ApplicationException,
        ) as ex:
            raise ex

        except Exception as ex:
            logger.info(ex)
            raise UnexpectedApplicationException(original_error=ex)
