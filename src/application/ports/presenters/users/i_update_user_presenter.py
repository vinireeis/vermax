from abc import ABC, abstractmethod

from src.application.data_types.responses.users.user_response import (
    UpdateUserResponse,
)


class IUpdateUserPresenter(ABC):
    @staticmethod
    @abstractmethod
    def create_output_response() -> UpdateUserResponse:
        pass
