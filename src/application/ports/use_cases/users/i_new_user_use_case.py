from abc import ABC, abstractmethod

from src.application.data_types.dtos.user_dto import UserDto
from src.application.data_types.requests.users.user_request import (
    NewUserRequest,
)


class INewUserUseCase(ABC):
    @abstractmethod
    async def create_new_user(
        self, new_user_request: NewUserRequest
    ) -> UserDto:
        pass
