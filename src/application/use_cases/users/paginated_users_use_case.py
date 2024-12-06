from witch_doctor import WitchDoctor

from src.application.data_types.dtos.user_dto import PaginatedUsersDto
from src.application.ports.presenters.users.i_get_users_presenter import (
    IGetUsersPresenter,
)
from src.application.ports.repositories.users.i_user_repository import (
    IUserRepository,
)
from src.application.ports.use_cases.users.i_paginated_users_use_case import (
    IPaginatedUsersUseCase,
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


class PaginatedUsersUseCase(IPaginatedUsersUseCase):
    @WitchDoctor.injection
    def __init__(
        self,
        get_users_presenter: IGetUsersPresenter,
        user_repository: IUserRepository,
    ):
        self._get_user_presenter = get_users_presenter
        self._user_repository = user_repository

    async def get_paginated_users(
        self, limit: int, offset: int
    ) -> PaginatedUsersDto:
        try:
            paginated_users_model = (
                await self._user_repository.get_paginated_users(
                    limit=limit, offset=offset
                )
            )

            paginated_users_dto = (
                self._get_user_presenter.from_paginated_model_to_dto(
                    model=paginated_users_model
                )
            )

            return paginated_users_dto

        except (
            AdapterException,
            DomainException,
            ExternalException,
            ApplicationException,
        ) as ex:
            raise ex

        except Exception as ex:
            raise UnexpectedApplicationException(original_error=ex)
