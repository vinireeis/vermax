from http import HTTPStatus

from src.domain.exceptions.base.exception import ApplicationException


class UnexpectedApplicationException(ApplicationException):
    def __init__(self, *args, **kwargs):
        self.msg = 'An unexpected error has occurred.'
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )


class UserNotFoundException(ApplicationException):
    def __init__(self, user_id, *args, **kwargs):
        self.msg = f'User with ID {user_id} not found.'
        self.status_code = HTTPStatus.NOT_FOUND

        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )
