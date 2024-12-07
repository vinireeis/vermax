from src.application.data_types.responses.users.user_response import (
    UpdateUserResponse,
)
from src.application.ports.presenters.users.i_update_user_presenter import (
    IUpdateUserPresenter,
)
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)


class UpdateUserPresenter(IUpdateUserPresenter):
    @staticmethod
    def create_output_response() -> UpdateUserResponse:
        try:
            response = UpdateUserResponse(
                success=True, message='User updated successfully'
            )

            return response

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)
