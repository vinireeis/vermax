from http import HTTPStatus

from decouple import config
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from src.adapters.controllers.home_broker_controller import (
    HomeBrokerController,
)
from src.application.data_types.requests.accounts.transfer_request import (
    TransferCashRequest,
)
from src.application.data_types.responses.accounts.accounts_response import (
    GetBalanceResponse,
    TransferCashResponse,
)


class AccountsRouter:
    _router = APIRouter(tags=['Accounts'])
    _oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl=f'{config("ROOT_PATH")}/token'
    )

    @classmethod
    def get_accounts_router(cls):
        return cls._router

    @staticmethod
    @_router.post(
        path='/accounts/transfer',
        status_code=HTTPStatus.OK,
        response_model=TransferCashResponse,
        response_model_exclude_none=True,
    )
    async def transfer_cash(
        request: TransferCashRequest, token: str = Depends(_oauth2_scheme)
    ) -> TransferCashResponse:
        response = await HomeBrokerController.transfer_cash(
            request=request, token=token
        )
        return response

    @staticmethod
    @_router.get(
        path='/accounts/balance',
        status_code=HTTPStatus.OK,
        response_model=GetBalanceResponse,
        response_model_exclude_none=True,
    )
    async def get_balance(
        token: str = Depends(_oauth2_scheme),
    ) -> TransferCashResponse:
        response = await HomeBrokerController.get_balance(token=token)
        return response
