from witch_doctor import WitchDoctor

from src.application.data_types.dtos.user_dto import UserDto
from src.application.data_types.responses.users.user_response import (
    NewUserRequest,
)
from src.application.ports.presenters.users.i_new_user_presenter import (
    INewUserPresenter,
)
from src.application.ports.repositories.users.i_user_repository import (
    IUserRepository,
)
from src.application.ports.use_cases.users.i_new_user_use_case import (
    INewUserUseCase,
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


class NewUserUseCase(INewUserUseCase):
    @WitchDoctor.injection
    def __init__(
        self,
        new_user_presenter: INewUserPresenter,
        user_repository: IUserRepository,
    ):
        self._new_user_presenter = new_user_presenter
        self._user_repository = user_repository

    async def create_new_user(
        self, new_user_request: NewUserRequest
    ) -> UserDto:
        try:
            user_entity = (
                self._new_user_presenter.from_input_request_to_entity(
                    request=new_user_request
                )
            )

            user_model = self._new_user_presenter.from_entity_to_model(
                entity=user_entity
            )

            await self._user_repository.insert_new_user(user_model=user_model)

            user_dto = self._new_user_presenter.from_model_to_dto(
                model=user_model
            )

            return user_dto

        except (
            AdapterException,
            DomainException,
            ExternalException,
            ApplicationException,
        ) as ex:
            raise ex

        except Exception as ex:
            raise UnexpectedApplicationException(original_error=ex)
