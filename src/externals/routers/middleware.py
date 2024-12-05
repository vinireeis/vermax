from http import HTTPStatus
from time import time

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from loguru import logger
from pydantic import ValidationError

from src.adapters.data_types.response.error_response import ErrorResponse
from src.domain.exceptions.adapters.exception import AdapterException
from src.domain.exceptions.application.exception import ApplicationException
from src.domain.exceptions.domain.exception import DomainException
from src.domain.exceptions.externals.exception import ExternalException


class Middleware:
    @staticmethod
    def register_middleware(app: FastAPI):
        @app.middleware('http')
        async def process_request(
            request: Request, call_next: callable
        ) -> Response:
            start_time = time()
            response = await Middleware._response_handler(
                request=request, call_next=call_next
            )
            process_time = time() - start_time
            response.headers['X-Process-Time'] = str(process_time)
            return response

    @staticmethod
    async def _response_handler(request: Request, call_next: callable):
        response = None

        try:
            response = await call_next(request)

        except (
            DomainException,
            ExternalException,
            AdapterException,
            ApplicationException,
        ) as ex:
            response = Middleware._build_error_response(
                status_code=ex.status_code, message=ex.msg, ex=ex
            )

        except ValidationError as ex:
            response = Middleware._build_error_response(
                status_code=HTTPStatus.BAD_REQUEST, ex=ex
            )

        except Exception as ex:
            response = Middleware._build_error_response(
                ex=ex,
                message='Unexpected error has occurred',
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            )

        finally:
            return response

    @staticmethod
    def _build_error_response(
        ex: Exception, message: str = None, status_code: HTTPStatus = None
    ) -> JSONResponse:
        logger.info(ex)

        error_response = ErrorResponse(
            success=False, message=message if message else str(ex)
        )

        response = JSONResponse(
            status_code=status_code
            if status_code
            else HTTPStatus.INTERNAL_SERVER_ERROR,
            content=error_response.model_dump(exclude_none=True),
        )

        return response
