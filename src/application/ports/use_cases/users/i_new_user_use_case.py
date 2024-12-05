from abc import abstractmethod

from src.application.data_types.dtos.user_dto import UserDto
from src.application.data_types.responses.users.user_response import (
    NewUserRequest,
)


class INewUserUseCase:
    @abstractmethod
    async def create_new_user(
        self, new_user_request: NewUserRequest
    ) -> UserDto:
        pass
