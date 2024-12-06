from abc import ABC, abstractmethod

from src.application.data_types.dtos.user_dto import UserDto
from src.application.data_types.requests.users.user_request import (
    NewUserRequest,
)
from src.application.data_types.responses.users.user_response import (
    NewUserResponse,
)
from src.domain.entities.user_entity import UserEntity
from src.domain.models.users.user_model import UserModel


class INewUserPresenter(ABC):
    @staticmethod
    @abstractmethod
    def from_input_request_to_entity(request: NewUserRequest) -> UserEntity:
        pass

    @staticmethod
    @abstractmethod
    def from_entity_to_model(entity: UserEntity) -> UserModel:
        pass

    @staticmethod
    @abstractmethod
    def from_model_to_dto(model: UserModel) -> UserDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_output_response(user_dto: UserDto) -> NewUserResponse:
        pass
