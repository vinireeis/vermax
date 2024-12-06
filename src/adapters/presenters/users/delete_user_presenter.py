from src.application.data_types.responses.users.user_response import (
    DeleteUserResponse,
)
from src.application.ports.presenters.users.i_delete_user_presenter import (
    IDeleteUserPresenter,
)
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)


class DeleteUserPresenter(IDeleteUserPresenter):
    @staticmethod
    def create_output_response() -> DeleteUserResponse:
        try:
            response = DeleteUserResponse(
                success=True, message='User deleted successfully'
            )

            return response

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)
