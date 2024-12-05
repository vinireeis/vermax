from abc import ABC, abstractmethod

from src.application.data_types.requests.users.user_request import (
    DeleteUserResponse,
)


class IDeleteUserPresenter(ABC):
    @staticmethod
    @abstractmethod
    def create_output_response() -> DeleteUserResponse:
        pass
