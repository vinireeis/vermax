from http import HTTPStatus


class BaseCustomException(Exception):
    def __init__(
        self,
        msg: str,
        status_code: HTTPStatus,
        success: bool,
        original_error: Exception = None,
        *args,
        **kwargs,
    ):
        self.msg = msg
        self.status_code = status_code
        self.success = success
        self.original_error = original_error
        super().__init__(msg, *args)


class DomainException(BaseCustomException):
    pass


class AdapterException(BaseCustomException):
    pass


class ApplicationException(BaseCustomException):
    pass


class ExternalException(BaseCustomException):
    pass
