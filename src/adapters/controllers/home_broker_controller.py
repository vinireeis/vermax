from fastapi.security import OAuth2PasswordRequestForm
from witch_doctor import WitchDoctor

from src.adapters.ports.controllers.i_home_broker_controller import (
    IHomeBrokerController,
)
from src.application.data_types.requests.users.user_request import (
    NewUserRequest,
)
from src.application.data_types.responses.auth.token_response import (
    GetTokenResponse,
)
from src.application.data_types.responses.users.user_response import (
    DeleteUserResponse,
    GetPaginatedUsersResponse,
    GetUserResponse,
    NewUserResponse,
)
from src.application.ports.presenters.auth.i_get_token_presenter import (
    IGetTokenPresenter,
)
from src.application.ports.presenters.users.i_delete_user_presenter import (
    IDeleteUserPresenter,
)
from src.application.ports.presenters.users.i_get_users_presenter import (
    IGetUsersPresenter,
)
from src.application.ports.presenters.users.i_new_user_presenter import (
    INewUserPresenter,
)
from src.application.ports.use_cases.auth.i_get_token_use_case import (
    IGetTokenUseCase,
)
from src.application.ports.use_cases.users.i_delete_user_use_case import (
    IDeleteUserUseCase,
)
from src.application.ports.use_cases.users.i_get_user_use_case import (
    IGetUserUseCase,
)
from src.application.ports.use_cases.users.i_new_user_use_case import (
    INewUserUseCase,
)
from src.application.ports.use_cases.users.i_paginated_users_use_case import (
    IPaginatedUsersUseCase,
)


class HomeBrokerController(IHomeBrokerController):
    @staticmethod
    @WitchDoctor.injection
    async def create_new_user(
        new_user_request: NewUserRequest,
        new_user_presenter: INewUserPresenter,
        new_user_use_case: INewUserUseCase,
    ) -> NewUserResponse:
        dto = await new_user_use_case.create_new_user(
            new_user_request=new_user_request
        )
        response = new_user_presenter.from_dto_to_output_response(user_dto=dto)

        return response

    @classmethod
    @WitchDoctor.injection
    async def get_user_by_id(
        cls,
        user_id: int,
        get_users_presenter: IGetUsersPresenter,
        get_user_use_case: IGetUserUseCase,
    ) -> GetUserResponse:
        dto = await get_user_use_case.get_user(user_id=user_id)
        response = get_users_presenter.from_dto_to_output_response(
            user_dto=dto
        )

        return response

    @classmethod
    @WitchDoctor.injection
    async def get_paginated_users(
        cls,
        limit: int,
        offset: int,
        get_users_presenter: IGetUsersPresenter,
        paginated_users_use_case: IPaginatedUsersUseCase,
    ) -> GetPaginatedUsersResponse:
        dto = await paginated_users_use_case.get_paginated_users(
            limit=limit, offset=offset
        )
        response = get_users_presenter.from_paginated_dto_to_output_response(
            paginated_users_dto=dto
        )
        return response

    @classmethod
    @WitchDoctor.injection
    async def delete_user_by_id(
        cls,
        user_id: int,
        delete_user_use_case: IDeleteUserUseCase,
        delete_user_presenter: IDeleteUserPresenter,
    ) -> DeleteUserResponse:
        await delete_user_use_case.delete_user(user_id=user_id)
        response = delete_user_presenter.create_output_response()

        return response

    @classmethod
    @WitchDoctor.injection
    async def get_token(
        cls,
        form_data: OAuth2PasswordRequestForm,
        get_token_use_case: IGetTokenUseCase,
        get_token_presenter: IGetTokenPresenter,
    ) -> GetTokenResponse:
        dto = await get_token_use_case.get_token(form_data=form_data)
        response = (
            get_token_presenter.from_access_token_dto_to_output_response(
                access_token_dto=dto
            )
        )
        return response
