from decouple import config
from fastapi import FastAPI

from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from src.externals.routers.users.router import UserRouter


class FastApiHttpServerConfigInfrastructure(IHttpServerConfigInfrastructure):
    def __init__(self):
        self.__root = config('ROOT_PATH')
        self.__app = FastAPI(
            title='Verrmax home broker API',
            description='A simple and secure Home broker API for managing'
            ' users accounts, deposits, balances, and asset'
            ' purchases.',
            docs_url=self.__root + '/docs',
            openapi_url=self.__root + '/openapi.json',
        )

    def __register_router(self):
        router = UserRouter.get_router()
        self.__app.include_router(router, prefix=self.__root)

    def set_http_server_config(self) -> FastAPI:
        self.__register_router()
        return self.__app
