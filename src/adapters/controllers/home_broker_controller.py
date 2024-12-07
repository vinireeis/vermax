from fastapi.security import OAuth2PasswordRequestForm
from witch_doctor import WitchDoctor

from src.adapters.ports.controllers.i_home_broker_controller import (
    IHomeBrokerController,
)
from src.application.data_types.requests.accounts.transfer_request import (
    TransferCashRequest,
)
from src.application.data_types.requests.users.user_request import (
    NewUserRequest,
    UpdateUserRequest,
)
from src.application.data_types.responses.accounts.accounts_response import (
    GetBalanceResponse,
    TransferCashResponse,
)
from src.application.data_types.responses.auth.token_response import (
    GetTokenResponse,
)
from src.application.data_types.responses.users.user_response import (
    DeleteUserResponse,
    GetPaginatedUsersResponse,
    GetUserResponse,
    NewUserResponse,
    UpdateUserResponse,
)
from src.application.ports.presenters.accounts.i_get_balance_presenter import (
    IGetBalancePresenter,
)
from src.application.ports.presenters.accounts.i_transfer_cash_presenter import (  # noqa: E501
    ITransferCashPresenter,
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
from src.application.ports.presenters.users.i_update_user_presenter import (
    IUpdateUserPresenter,
)
from src.application.ports.services.token.i_token_service import ITokenService
from src.application.ports.use_cases.accounts.i_get_balance_use_case import (
    IGetBalanceUseCase,
)
from src.application.ports.use_cases.accounts.i_transfer_cash_use_case import (
    ITransferCashUseCase,
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
from src.application.ports.use_cases.users.i_update_user_use_case import (
    IUpdateUserUseCase,
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
        jwt_token_service: ITokenService,
        token: str,
    ) -> GetUserResponse:
        await jwt_token_service.validate_token(jwt=token)
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
    async def update_user_by_id(  # noqa: PLR0917, PLR0913
        cls,
        user_id: int,
        token: str,
        update_user_request: UpdateUserRequest,
        update_user_use_case: IUpdateUserUseCase,
        update_user_presenter: IUpdateUserPresenter,
        jwt_token_service: ITokenService,
    ) -> UpdateUserResponse:
        await jwt_token_service.validate_token(jwt=token)
        await update_user_use_case.update_user(
            update_user_request=update_user_request, user_id=user_id
        )
        response = update_user_presenter.create_output_response()

        return response

    @classmethod
    @WitchDoctor.injection
    async def delete_user_by_id(
        cls,
        user_id: int,
        delete_user_use_case: IDeleteUserUseCase,
        delete_user_presenter: IDeleteUserPresenter,
        jwt_token_service: ITokenService,
        token: str,
    ) -> DeleteUserResponse:
        await jwt_token_service.validate_token(jwt=token)
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

    @classmethod
    @WitchDoctor.injection
    async def transfer_cash(
        cls,
        transfer_cash_use_case: ITransferCashUseCase,
        transfer_cash_presenter: ITransferCashPresenter,
        request: TransferCashRequest,
    ) -> TransferCashResponse:
        dto = await transfer_cash_use_case.transfer_cash(request=request)
        response = (
            transfer_cash_presenter.from_transaction_dto_to_output_response(
                dto=dto
            )
        )
        return response

    @classmethod
    @WitchDoctor.injection
    async def get_balance(
        cls,
        token: str,
        jwt_token_service: ITokenService,
        get_balance_use_case: IGetBalanceUseCase,
        get_balance_presenter: IGetBalancePresenter,
    ) -> GetBalanceResponse:
        await jwt_token_service.validate_token(jwt=token)
        decoded_token_dto = await jwt_token_service.decode_token(jwt=token)
        dto = await get_balance_use_case.get_user_balance(
            decoded_token_dto=decoded_token_dto
        )
        response = (
            get_balance_presenter.from_transaction_dto_to_output_response(
                dto=dto
            )
        )
        return response
