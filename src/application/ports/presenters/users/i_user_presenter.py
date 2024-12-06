from abc import ABC, abstractmethod

from src.domain.entities.user_entity import UserEntity
from src.domain.models.users.user_model import UserModel


class IUserPresenter(ABC):
    @staticmethod
    @abstractmethod
    def from_model_to_entity(
        user_model: UserModel, password: str
    ) -> UserEntity:
        pass
