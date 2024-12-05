from abc import abstractmethod, ABC

from src.application.data_types.dtos.user_dto import UserDto


class IGetUserUseCase(ABC):

    @abstractmethod
    async def get_user(self, user_id: int) -> UserDto:
        pass
