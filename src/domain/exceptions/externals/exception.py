from http import HTTPStatus

from src.domain.exceptions.base.exception import ExternalException


class SqlAlchemyInfrastructureException(ExternalException):
    def __init__(self, *args, **kwargs):
        self.msg = 'Error trying to get session'
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        self.success = False
        super().__init__(
            self.msg, self.status_code, self.success, *args, **kwargs
        )


class UnexpectedInfrastructureException(ExternalException):
    def __init__(self, *args, **kwargs):
        self.msg = 'Unexpected infrastructure exception'
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        self.success = False
        self.original_error = None
        super().__init__(
            self.msg,
            self.status_code,
            self.success,
            self.original_error,
            *args,
            **kwargs,
        )
