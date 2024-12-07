from http import HTTPStatus

from src.domain.exceptions.base.exception import AdapterException


class UserNotFoundException(AdapterException):
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


class UserEmailNotFoundException(AdapterException):
    def __init__(self, *args, **kwargs):
        self.msg = 'Verify email or password and try again.'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )


class UserNotFoundByAccountIdException(AdapterException):
    def __init__(self, *args, **kwargs):
        self.msg = 'User account not found.'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )


class CpfAlreadyExistsException(AdapterException):
    def __init__(self, *args, **kwargs):
        self.msg = 'User with this cpf already exists.'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )


class EmailAlreadyExistsException(AdapterException):
    def __init__(self, *args, **kwargs):
        self.msg = 'User with this email already exists.'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )


class UnexpectedPresenterException(AdapterException):
    def __init__(self, original_error=None, *args, **kwargs):
        self.msg = 'An unexpected error trying to convert some data.'
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        self.success = False
        self.original_error = original_error
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            self.original_error,
            *args,
            **kwargs,
        )


class UnexpectedRepositoryException(AdapterException):
    def __init__(self, original_error=None, *args, **kwargs):
        self.msg = (
            'An unexpected error occurred while trying to use the repository.'
        )
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        self.success = False
        self.original_error = original_error
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            self.original_error,
            *args,
            **kwargs,
        )
