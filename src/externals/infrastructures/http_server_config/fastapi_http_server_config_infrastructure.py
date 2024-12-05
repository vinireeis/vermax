from decouple import config
from fastapi import FastAPI

from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from src.externals.routers.middleware import Middleware
from src.externals.routers.users.router import UserRouter


class FastApiHttpServerConfigInfrastructure(IHttpServerConfigInfrastructure):
    def __init__(self):
        self._root = config('ROOT_PATH')
        self._app = FastAPI(
            title='Vermax home broker API',
            description='A simple and secure Home broker API for managing'
            ' users accounts, deposits, balances, and asset'
            ' purchases.',
            docs_url=self._root + '/docs',
            openapi_url=self._root + '/openapi.json',
        )

    def _register_router(self):
        router = UserRouter.get_router()
        self._app.include_router(router, prefix=self._root)

    def _register_middlewares(self):
        Middleware.set_middleware(app=self._app)

    def set_http_server_config(self) -> FastAPI:
        self._register_router()
        self._register_middlewares()
        return self._app
