from abc import ABC, abstractmethod

from src.application.data_types.dtos.user_dto import UserDto, PaginatedUsersDto
from src.application.data_types.requests.users.user_request import (
    GetUserResponse, GetPaginatedUserResponse
)

from src.domain.models.users.user_model import UserModel, PaginatedUsersModel


class IGetUsersPresenter(ABC):

    @staticmethod
    @abstractmethod
    def from_model_to_dto(model: UserModel) -> UserDto:
        pass

    @staticmethod
    @abstractmethod
    def from_paginated_model_to_dto(model: PaginatedUsersModel) -> PaginatedUsersDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_output_response(user_dto: UserDto) -> GetUserResponse:
        pass

    @staticmethod
    @abstractmethod
    def from_paginated_dto_to_output_response(user_dto: UserDto) -> GetPaginatedUserResponse:
        pass
