from abc import ABC, abstractmethod

from src.application.data_types.dtos.user_dto import PaginatedUsersDto


class IPaginatedUsersUseCase(ABC):
    @abstractmethod
    async def get_paginated_users(
        self, limit: int, offset: int
    ) -> PaginatedUsersDto:
        pass
