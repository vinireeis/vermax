from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.adapters.controllers.home_broker_controller import (
    HomeBrokerController,
)
from src.application.data_types.responses.auth.token_response import (
    GetTokenResponse,
)


class AuthRouter:
    __router = APIRouter(tags=['Authentication'])

    @classmethod
    def get_auth_router(cls):
        return cls.__router

    @staticmethod
    @__router.post(
        path='/token',
        status_code=HTTPStatus.CREATED,
        response_model=GetTokenResponse,
    )
    async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
        response = await HomeBrokerController.get_token(form_data=form_data)
        return response
