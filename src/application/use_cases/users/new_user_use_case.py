from src.application.data_types.dtos.user_dto import UserDto
from src.application.data_types.responses.users.user_response import (
    NewUserRequest,
)
from src.application.ports.presenters.users.i_new_user_presenter import (
    INewUserPresenter,
)
from src.application.ports.use_cases.users.i_new_user_use_case import (
    INewUserUseCase,
)


class NewUserUseCase(INewUserUseCase):
    __new_user_presenter: INewUserPresenter

    def __init__(
        self,
        new_user_presenter: INewUserPresenter,
    ):
        self.__new_user_presenter = new_user_presenter

    @classmethod
    async def create_new_user(
        self, new_user_request: NewUserRequest
    ) -> UserDto:
        user_entity = self.__new_user_presenter.from_input_request_to_entity(
            request=new_user_request
        )

        user_dto = self.__new_user_presenter.from_model_to_dto(
            entity=user_entity
        )

        return self.__new_user_presenter.from_dto_to_output_response(
            user_dto=user_dto
        )
        pass
