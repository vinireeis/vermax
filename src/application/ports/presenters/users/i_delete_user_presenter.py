from abc import ABC, abstractmethod

from src.application.data_types.responses.users.user_response import (
    DeleteUserResponse,
)


class IDeleteUserPresenter(ABC):
    @staticmethod
    @abstractmethod
    def create_output_response() -> DeleteUserResponse:
        pass
