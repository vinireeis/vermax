from src.application.data_types.dtos.user_dto import UserDto
from src.application.data_types.requests.users.user_request import (
    NewUserPayload,
    NewUserResponse,
)
from src.application.data_types.responses.users.user_response import (
    NewUserRequest,
)
from src.application.ports.presenters.users.i_new_user_presenter import (
    INewUserPresenter,
)
from src.domain.entities.user_entity import UserEntity
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)
from src.domain.models.accounts.account_model import AccountModel
from src.domain.models.users.user_model import UserModel


class NewUserPresenter(INewUserPresenter):
    @staticmethod
    def from_input_request_to_entity(request: NewUserRequest) -> UserEntity:
        try:
            entity = UserEntity(
                name=request.name,
                email=str(request.email),
                password=request.password,
                cpf=request.cpf,
            )
            return entity

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_entity_to_model(entity: UserEntity) -> UserModel:
        try:

            account_model = AccountModel(
                account_id=entity.account_id,
            )

            user_model = UserModel(
                name=entity.name,
                email=entity.email,
                password=entity.password_hash,
                cpf=entity.cpf,
                account_id=entity.account_id,
                account=account_model
            )
            return user_model

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_model_to_dto(model: UserModel) -> UserDto:
        try:
            user_dto = UserDto(
                id=model.id,
                name=model.name,
                email=model.email,
                cpf=model.cpf,
                account_id=model.account_id,
            )
            return user_dto

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_dto_to_output_response(user_dto: UserDto) -> NewUserResponse:
        try:
            new_user_payload = NewUserPayload(
                account_id=user_dto.account_id,
            )

            response = NewUserResponse(payload=new_user_payload, success=True)
            return response

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)
