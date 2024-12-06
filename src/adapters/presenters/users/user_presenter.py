from src.application.ports.presenters.users.i_user_presenter import (
    IUserPresenter,
)
from src.domain.entities.user_entity import UserEntity
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)
from src.domain.models.users.user_model import UserModel


class UserPresenter(IUserPresenter):
    @staticmethod
    def from_model_to_entity(
        user_model: UserModel, password: str
    ) -> UserEntity:
        try:
            entity = UserEntity(
                name=user_model.name,
                email=user_model.email,
                password=password,
                password_hash=user_model.password,
                cpf=user_model.cpf,
                account_id=user_model.account_id,
            )
            return entity

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)
