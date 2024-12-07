from http import HTTPStatus

from decouple import config
from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordBearer

from src.adapters.controllers.home_broker_controller import (
    HomeBrokerController,
)
from src.application.data_types.requests.users.user_request import (
    NewUserRequest, UpdateUserRequest,
)
from src.application.data_types.responses.users.user_response import (
    DeleteUserResponse,
    GetPaginatedUsersResponse,
    GetUserResponse,
    NewUserResponse,
    UpdateUserResponse,
)


class UserRouter:
    _router = APIRouter(tags=['Users'])
    _oauth2_scheme = OAuth2PasswordBearer(
        tokenUrl=f'{config("ROOT_PATH")}/token'
    )

    @classmethod
    def get_user_router(cls):
        return cls._router

    @staticmethod
    @_router.post(
        path='/users',
        status_code=HTTPStatus.CREATED,
        response_model=NewUserResponse,
        response_model_exclude_none=True,
    )
    async def create_user(request: NewUserRequest) -> NewUserResponse:
        response = await HomeBrokerController.create_new_user(
            new_user_request=request
        )
        return response

    @staticmethod
    @_router.get(
        path='/users',
        status_code=HTTPStatus.OK,
        response_model=GetPaginatedUsersResponse,
        response_model_exclude_none=True,
    )
    async def get_paginated_users(
        limit: int = Query(default=10, ge=1),
        offset: int = Query(default=0, ge=0),
    ) -> GetPaginatedUsersResponse:
        response = await HomeBrokerController.get_paginated_users(
            limit=limit, offset=offset
        )
        return response

    @staticmethod
    @_router.get(
        path='/users/{user_id}',
        status_code=HTTPStatus.OK,
        response_model=GetUserResponse,
        response_model_exclude_none=True,
    )
    async def get_user(
        user_id: int, token: str = Depends(_oauth2_scheme)
    ) -> GetUserResponse:
        response = await HomeBrokerController.get_user_by_id(
            user_id=user_id, token=token
        )
        return response

    @staticmethod
    @_router.put(
        path='/users/{user_id}',
        status_code=HTTPStatus.OK,
        response_model=UpdateUserResponse,
        response_model_exclude_none=True,
    )
    async def update_user(
        request: UpdateUserRequest,
        user_id: int,
        token: str = Depends(_oauth2_scheme),
    ) -> UpdateUserResponse:
        response = await HomeBrokerController.update_user_by_id(
            user_id=user_id, token=token, update_user_request=request
        )
        return response

    @staticmethod
    @_router.delete(
        path='/users/{user_id}',
        status_code=HTTPStatus.OK,
        response_model=DeleteUserResponse,
        response_model_exclude_none=True,
    )
    async def delete_user(
        user_id: int,
        token: str = Depends(_oauth2_scheme),
    ) -> DeleteUserResponse:
        response = await HomeBrokerController.delete_user_by_id(
            user_id=user_id, token=token
        )
        return response
