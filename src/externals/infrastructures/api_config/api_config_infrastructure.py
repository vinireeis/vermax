from fastapi import FastAPI
from witch_doctor import WitchDoctor

from src.externals.ports.infrastructures.i_api_config_infrastructure import (
    IApiConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)


class ApiConfigInfrastructure(IApiConfigInfrastructure):
    @staticmethod
    @WitchDoctor.injection
    def start_app(
        http_server_config: IHttpServerConfigInfrastructure,
        logs_config: ILogsConfigInfrastructure,
    ) -> FastAPI:
        logs_config.set_logger_config()
        app = http_server_config.set_http_server_config()

        return app
