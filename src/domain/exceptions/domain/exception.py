from http import HTTPStatus

from src.domain.exceptions.base.exception import DomainException


class InvalidPassword(DomainException):
    def __init__(self, *args, **kwargs):
        self.msg = 'Verify email or password'
        self.status_code = HTTPStatus.BAD_REQUEST
        self.success = False
        super().__init__(
            self.msg, self.status_code, self.success, *args, **kwargs
        )


class FailToGeneratePasswordHash(DomainException):
    def __init__(self, *args, **kwargs):
        self.msg = 'Fail to generate pw hash'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        self.success = False
        super().__init__(
            self.msg, self.status_code, self.success, *args, **kwargs
        )
