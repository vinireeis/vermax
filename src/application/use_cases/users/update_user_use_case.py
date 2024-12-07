from witch_doctor import WitchDoctor

from src.application.data_types.requests.users.user_request import (
    UpdateUserRequest,
)
from src.application.ports.repositories.users.i_user_repository import (
    IUserRepository,
)
from src.application.ports.use_cases.users.i_update_user_use_case import (
    IUpdateUserUseCase,
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


class UpdateUserUseCase(IUpdateUserUseCase):
    @WitchDoctor.injection
    def __init__(
        self,
        user_repository: IUserRepository,
    ):
        self._user_repository = user_repository

    async def update_user(
        self, update_user_request: UpdateUserRequest, user_id: int
    ):
        try:
            await self._user_repository.update_user_by_id(
                user_id=user_id, update_user_request=update_user_request
            )

        except (
            AdapterException,
            DomainException,
            ExternalException,
            ApplicationException,
        ) as ex:
            raise ex

        except Exception as ex:
            raise UnexpectedApplicationException(original_error=ex)
