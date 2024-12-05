from witch_doctor import WitchDoctor

from src.adapters.ports.i_home_broker_controller import IHomeBrokerController
from src.application.data_types.requests.users.user_request import (
    DeleteUserResponse,
    GetPaginatedUserResponse,
    GetUserResponse,
    NewUserResponse,
)
from src.application.data_types.responses.users.user_response import (
    NewUserRequest,
)
from src.application.ports.presenters.users.i_new_user_presenter import (
    INewUserPresenter,
)
from src.application.ports.use_cases.users.i_new_user_use_case import (
    INewUserUseCase,
)


class HomeBrokerController(IHomeBrokerController):
    __new_user_presenter: INewUserPresenter
    __new_user_use_case: INewUserUseCase

    @WitchDoctor.injection
    def __init__(
        self,
        new_user_presenter: INewUserPresenter,
        new_user_use_case: INewUserUseCase,
    ):
        self.__new_user_presenter = new_user_presenter
        self.__new_user_use_case = new_user_use_case

    @classmethod
    async def create_new_user(
        cls, new_user_request: NewUserRequest
    ) -> NewUserResponse:
        pass

    @classmethod
    async def get_user_by_id(cls, user_id: int) -> GetUserResponse:
        pass

    @classmethod
    async def get_paginated_users(
        cls, limit: int, offset: int
    ) -> list[GetPaginatedUserResponse]:
        pass

    @classmethod
    async def delete_user_by_id(cls, user_id: int) -> DeleteUserResponse:
        pass
