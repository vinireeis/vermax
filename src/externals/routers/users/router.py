from http import HTTPStatus
from uuid import UUID

from fastapi import APIRouter, Query

from src.adapters.controllers.home_broker_controller import (
    HomeBrokerController,
)
from src.application.data_types.requests.users.user_request import (
    DeleteUserResponse,
    GetPaginatedUserResponse,
    NewUserResponse,
)
from src.application.data_types.responses.users.user_response import (
    NewUserRequest,
)


class UserRouter:
    __router = APIRouter(tags=['Users'])

    @classmethod
    def get_router(cls):
        return cls.__router

    @staticmethod
    @__router.post(
        path='/users',
        status_code=HTTPStatus.CREATED,
        response_model=NewUserResponse,
        response_model_exclude_none=True,
    )
    async def create_user(request: NewUserRequest) -> NewUserResponse:
        response = HomeBrokerController.create_new_user(
            new_user_request=request
        )
        return response

    @staticmethod
    @__router.get(
        path='/users',
        status_code=HTTPStatus.OK,
        response_model=GetPaginatedUserResponse,
        response_model_exclude_none=True,
    )
    async def get_paginated_users(
        limit: int = Query(default=10, ge=1),
        offset: int = Query(default=0, ge=0),
    ) -> GetPaginatedUserResponse:
        pass

    @staticmethod
    @__router.delete(
        path='/users/{user_id}',
        status_code=HTTPStatus.NO_CONTENT,
        response_model=DeleteUserResponse,
        response_model_exclude_none=True,
    )
    async def delete_user(user_id: UUID) -> DeleteUserResponse:
        pass
