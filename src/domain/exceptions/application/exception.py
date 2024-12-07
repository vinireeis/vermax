from http import HTTPStatus

from src.domain.exceptions.base.exception import ApplicationException


class UnexpectedApplicationException(ApplicationException):
    def __init__(self, original_error=None, *args, **kwargs):
        self.msg = 'An unexpected error has occurred.'
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


class TokenExpiredException(ApplicationException):
    def __init__(self, *args, **kwargs):
        self.msg = 'Token expired.'
        self.status_code = HTTPStatus.UNAUTHORIZED
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )


class InvalidTokenException(ApplicationException):
    def __init__(self, *args, **kwargs):
        self.msg = 'Invalid token.'
        self.status_code = HTTPStatus.UNAUTHORIZED
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )


class UserNotFoundException(ApplicationException):
    def __init__(self, *args, **kwargs):
        self.msg = 'User with this id not found.'
        self.status_code = HTTPStatus.NOT_FOUND
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )


class TransferOperationNotAllowedException(ApplicationException):
    def __init__(self, *args, **kwargs):
        self.msg = 'The origin account does not belong to the same user/CPF.'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        self.success = False
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            *args,
            **kwargs,
        )
