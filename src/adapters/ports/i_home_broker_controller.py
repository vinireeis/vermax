from abc import ABC, abstractmethod

from src.application.data_types.requests.users.user_request import (
    DeleteUserResponse,
    GetPaginatedUserResponse,
    GetUserResponse,
    NewUserResponse,
)
from src.application.data_types.responses.users.user_response import (
    NewUserRequest,
)


class IHomeBrokerController(ABC):
    @classmethod
    @abstractmethod
    async def create_new_user(
        cls, new_user_request: NewUserRequest
    ) -> NewUserResponse:
        pass

    @classmethod
    @abstractmethod
    async def get_user_by_id(cls, user_id: int) -> GetUserResponse:
        pass

    @classmethod
    @abstractmethod
    async def get_paginated_users(
        cls, limit: int, offset: int
    ) -> list[GetPaginatedUserResponse]:
        pass

    @classmethod
    @abstractmethod
    async def delete_user_by_id(cls, user_id: int) -> DeleteUserResponse:
        pass
