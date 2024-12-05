from abc import ABC, abstractmethod

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
    async def get_paginated_users(
        cls, limit: int, offset: int
    ) -> PaginatedUsersModel:
        pass

    @classmethod
    @abstractmethod
    async def update_user_by_id(
        cls, user_id: int, user_model: UserModel
    ) -> UserModel:
        pass

    @classmethod
    async def delete_user_by_id(cls, user_id: int) -> bool:
        pass
