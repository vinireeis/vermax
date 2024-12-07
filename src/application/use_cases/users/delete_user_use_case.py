from witch_doctor import WitchDoctor

from src.application.ports.repositories.users.i_user_repository import (
    IUserRepository,
)
from src.application.ports.use_cases.users.i_delete_user_use_case import (
    IDeleteUserUseCase,
)
from src.domain.exceptions.application.exception import (
    UnexpectedApplicationException,
    UserNotFoundException,
)
from src.domain.exceptions.base.exception import (
    AdapterException,
    ApplicationException,
    DomainException,
    ExternalException,
)


class DeleteUserUseCase(IDeleteUserUseCase):
    @WitchDoctor.injection
    def __init__(
        self,
        user_repository: IUserRepository,
    ):
        self._user_repository = user_repository

    async def delete_user(self, user_id: int):
        try:
            user_has_deleted = await self._user_repository.delete_user_by_id(
                user_id=user_id
            )

            if not user_has_deleted:
                raise UserNotFoundException()

        except (
            AdapterException,
            DomainException,
            ExternalException,
            ApplicationException,
        ) as ex:
            raise ex

        except Exception as ex:
            raise UnexpectedApplicationException(original_error=ex)
