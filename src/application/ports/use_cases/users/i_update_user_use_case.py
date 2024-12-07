from abc import ABC, abstractmethod

from src.application.data_types.requests.users.user_request import (
    UpdateUserRequest,
)


class IUpdateUserUseCase(ABC):
    @abstractmethod
    async def update_user(
        self, update_user_request: UpdateUserRequest, user_id: int
    ):
        pass
