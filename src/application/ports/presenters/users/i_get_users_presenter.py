from abc import ABC, abstractmethod

from src.application.data_types.dtos.user_dto import PaginatedUsersDto, UserDto
from src.application.data_types.responses.users.user_response import (
    GetPaginatedUsersResponse,
    GetUserResponse,
)
from src.domain.models.users.user_model import PaginatedUsersModel, UserModel


class IGetUsersPresenter(ABC):
    @staticmethod
    @abstractmethod
    def from_model_to_dto(model: UserModel) -> UserDto:
        pass

    @staticmethod
    @abstractmethod
    def from_paginated_model_to_dto(
        model: PaginatedUsersModel,
    ) -> PaginatedUsersDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_output_response(user_dto: UserDto) -> GetUserResponse:
        pass

    @staticmethod
    @abstractmethod
    def from_paginated_dto_to_output_response(
        paginated_users_dto: PaginatedUsersDto,
    ) -> GetPaginatedUsersResponse:
        pass
