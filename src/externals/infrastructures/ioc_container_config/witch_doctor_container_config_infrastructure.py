from witch_doctor import InjectionType, WitchDoctor

from src.externals.infrastructures.api_config.api_config_infrastructure import (  # noqa: E501
    ApiConfigInfrastructure,
)
from src.externals.infrastructures.http_server_config.fastapi_http_server_config_infrastructure import (  # noqa: E501
    FastApiHttpServerConfigInfrastructure,
)
from src.externals.infrastructures.logs_config.loguru_config_infrastructure import (  # noqa: E501
    LoguruConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_api_config_infrastructure import (
    IApiConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_ioc_container_config_infrastructure import (  # noqa: E501
    IIocContainerConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_logs_config_infrastructure import (
    ILogsConfigInfrastructure,
)


class WitchDoctorContainerConfigInfrastructure(
    IIocContainerConfigInfrastructure
):
    @classmethod
    def __create_use_cases_container(cls):
        use_cases_container = WitchDoctor.container('use_cases')

        return use_cases_container

    @classmethod
    def __create_infrastructures_container(cls):
        infrastructures_container = WitchDoctor.container('infrastructures')

        infrastructures_container(
            IApiConfigInfrastructure,
            ApiConfigInfrastructure,
            InjectionType.SINGLETON,
        )
        infrastructures_container(
            IHttpServerConfigInfrastructure,
            FastApiHttpServerConfigInfrastructure,
            InjectionType.SINGLETON,
        )
        infrastructures_container(
            ILogsConfigInfrastructure,
            LoguruConfigInfrastructure,
            InjectionType.SINGLETON,
        )

        return infrastructures_container

    @classmethod
    def __create_repositories_container(cls):
        repositories_container = WitchDoctor.container('repositories')

        return repositories_container

    @classmethod
    def __create_presenters_container(cls):
        extensions_container = WitchDoctor.container('presenters')

        return extensions_container

    @classmethod
    def __create_containers(cls):
        cls.__create_use_cases_container()
        cls.__create_infrastructures_container()
        cls.__create_repositories_container()
        cls.__create_presenters_container()

    @classmethod
    def __load_containers(cls):
        WitchDoctor.load_container('use_cases')
        WitchDoctor.load_container('infrastructures')
        WitchDoctor.load_container('repositories')
        WitchDoctor.load_container('presenters')

    @classmethod
    def build_ioc_container(cls):
        cls.__create_containers()
        cls.__load_containers()
