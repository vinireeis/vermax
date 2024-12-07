from abc import ABC, abstractmethod
from uuid import UUID

from src.application.data_types.requests.users.user_request import (
    UpdateUserRequest,
)
from src.domain.models.users.user_model import PaginatedUsersModel, UserModel


class IUserRepository(ABC):
    @classmethod
    @abstractmethod
    async def insert_new_user(cls, user_model: UserModel) -> UserModel:
        pass

    @classmethod
    @abstractmethod
    async def get_user_by_id(cls, user_id: int) -> UserModel:
        pass

    @classmethod
    @abstractmethod
    async def get_user_by_email(cls, email: str) -> UserModel:
        pass

    @classmethod
    @abstractmethod
    async def get_user_by_account_id(cls, account_id: UUID) -> UserModel:
        pass

    @classmethod
    @abstractmethod
    async def get_paginated_users(
        cls, limit: int, offset: int
    ) -> PaginatedUsersModel:
        pass

    @classmethod
    @abstractmethod
    async def update_user_by_id(
        cls, user_id: int, update_user_request: UpdateUserRequest
    ):
        pass

    @classmethod
    async def delete_user_by_id(cls, user_id: int) -> bool:
        pass
