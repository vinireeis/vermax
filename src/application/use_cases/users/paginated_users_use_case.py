from witch_doctor import WitchDoctor

from src.application.data_types.dtos.user_dto import UserDto
from src.application.data_types.responses.users.user_response import (
    NewUserRequest,
)
from src.application.ports.presenters.users.i_get_users_presenter import IGetUsersPresenter
from src.application.ports.presenters.users.i_new_user_presenter import (
    INewUserPresenter,
)
from src.application.ports.repositories.users.i_user_repository import IUserRepository
from src.application.ports.use_cases.users.i_get_user_use_case import IGetUserUseCase
from src.application.ports.use_cases.users.i_new_user_use_case import (
    INewUserUseCase,
)
from src.domain.exceptions.application.exception import UnexpectedApplicationException
from src.domain.exceptions.base.exception import AdapterException, DomainException, ExternalException, \
    ApplicationException


class GetUserUseCase(IGetUserUseCase):

    @WitchDoctor.injection
    def __init__(
        self,
        get_users_presenter: IGetUsersPresenter,
        user_repository: IUserRepository,
    ):
        self._get_user_presenter = get_users_presenter
        self._user_repository = user_repository

    async def get_user(self, user_id: int) -> UserDto:
        try:
            user_model = await self._user_repository.get_user_by_id(
                user_id=user_id
            )

            user_dto = self._get_user_presenter.from_model_to_dto(
                model=user_model
            )

            return user_dto

        except (
                AdapterException, DomainException,
                ExternalException, ApplicationException
                ) as ex:
            raise ex

        except Exception as ex:
            raise UnexpectedApplicationException(original_error=ex)
