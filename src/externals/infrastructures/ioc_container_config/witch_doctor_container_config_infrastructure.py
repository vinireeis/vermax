from witch_doctor import InjectionType, WitchDoctor

from src.adapters.presenters.accounts.transfer_cash_presenter import (
    TransferCashPresenter,
)
from src.adapters.presenters.auth.get_token_presenter import GetTokenPresenter
from src.adapters.presenters.auth.jwt_presenter import JwtPresenter
from src.adapters.presenters.users.delete_user_presenter import (
    DeleteUserPresenter,
)
from src.adapters.presenters.users.get_users_presenter import GetUsersPresenter
from src.adapters.presenters.users.new_user_presenter import NewUserPresenter
from src.adapters.presenters.users.user_presenter import UserPresenter
from src.adapters.repositories.accounts.accounts_repository import (
    AccountsRepository,
)
from src.adapters.repositories.users.user_repository import UserRepository
from src.application.ports.presenters.accounts.i_transfer_cash_presenter import (
    ITransferCashPresenter,
)
from src.application.ports.presenters.auth.i_get_token_presenter import (
    IGetTokenPresenter,
)
from src.application.ports.presenters.auth.i_jwt_presenter import IJwtPresenter
from src.application.ports.presenters.users.i_delete_user_presenter import (
    IDeleteUserPresenter,
)
from src.application.ports.presenters.users.i_get_users_presenter import (
    IGetUsersPresenter,
)
from src.application.ports.presenters.users.i_new_user_presenter import (
    INewUserPresenter,
)
from src.application.ports.presenters.users.i_user_presenter import (
    IUserPresenter,
)
from src.application.ports.repositories.accounts.accounts_repository import (
    IAccountsRepository,
)
from src.application.ports.repositories.users.i_user_repository import (
    IUserRepository,
)
from src.application.ports.services.token.i_token_service import ITokenService
from src.application.ports.use_cases.accounts.i_transfer_cash_use_case import (
    ITransferCashUseCase,
)
from src.application.ports.use_cases.auth.i_get_token_use_case import (
    IGetTokenUseCase,
)
from src.application.ports.use_cases.users.i_delete_user_use_case import (
    IDeleteUserUseCase,
)
from src.application.ports.use_cases.users.i_get_user_use_case import (
    IGetUserUseCase,
)
from src.application.ports.use_cases.users.i_new_user_use_case import (
    INewUserUseCase,
)
from src.application.ports.use_cases.users.i_paginated_users_use_case import (
    IPaginatedUsersUseCase,
)
from src.application.services.token.jwt_token_service import JwtTokenService
from src.application.use_cases.accounts.transfer_cash_use_case import (
    TransferCashUseCase,
)
from src.application.use_cases.auth.get_token_use_case import GetTokenUseCase
from src.application.use_cases.users.delete_user_use_case import (
    DeleteUserUseCase,
)
from src.application.use_cases.users.get_user_use_case import GetUserUseCase
from src.application.use_cases.users.new_user_use_case import NewUserUseCase
from src.application.use_cases.users.paginated_users_use_case import (
    PaginatedUsersUseCase,
)
from src.externals.infrastructures.api_config.api_config_infrastructure import (
    ApiConfigInfrastructure,
)
from src.externals.infrastructures.db_config.sqlalchemy_config_infrastructure import (
    PostgresSqlAlchemyInfrastructure,
)
from src.externals.infrastructures.http_server_config.fastapi_http_server_config_infrastructure import (
    FastApiHttpServerConfigInfrastructure,
)
from src.externals.infrastructures.logs_config.loguru_config_infrastructure import (
    LoguruConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_api_config_infrastructure import (
    IApiConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_db_config_infrastructure import (
    IDbConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_http_config_infrastructure import (
    IHttpServerConfigInfrastructure,
)
from src.externals.ports.infrastructures.i_ioc_container_config_infrastructure import (
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

        use_cases_container(
            INewUserUseCase,
            NewUserUseCase,
            InjectionType.SINGLETON,
        )
        use_cases_container(
            IGetUserUseCase,
            GetUserUseCase,
            InjectionType.SINGLETON,
        )
        use_cases_container(
            IPaginatedUsersUseCase,
            PaginatedUsersUseCase,
            InjectionType.SINGLETON,
        )
        use_cases_container(
            IDeleteUserUseCase,
            DeleteUserUseCase,
            InjectionType.SINGLETON,
        )
        use_cases_container(
            IGetTokenUseCase,
            GetTokenUseCase,
            InjectionType.SINGLETON,
        )
        use_cases_container(
            ITransferCashUseCase,
            TransferCashUseCase,
            InjectionType.SINGLETON,
        )

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
        infrastructures_container(
            IDbConfigInfrastructure,
            PostgresSqlAlchemyInfrastructure,
            InjectionType.SINGLETON,
        )

        return infrastructures_container

    @classmethod
    def __create_repositories_container(cls):
        repositories_container = WitchDoctor.container('repositories')

        repositories_container(
            IUserRepository,
            UserRepository,
            InjectionType.SINGLETON,
        )
        repositories_container(
            IAccountsRepository,
            AccountsRepository,
            InjectionType.SINGLETON,
        )

        return repositories_container

    @classmethod
    def __create_services_container(cls):
        services_container = WitchDoctor.container('services')

        services_container(
            ITokenService,
            JwtTokenService,
            InjectionType.SINGLETON,
        )

        return services_container

    @classmethod
    def __create_presenters_container(cls):
        presenters_container = WitchDoctor.container('presenters')

        presenters_container(
            INewUserPresenter,
            NewUserPresenter,
            InjectionType.SINGLETON,
        )
        presenters_container(
            IGetUsersPresenter,
            GetUsersPresenter,
            InjectionType.SINGLETON,
        )
        presenters_container(
            IDeleteUserPresenter,
            DeleteUserPresenter,
            InjectionType.SINGLETON,
        )
        presenters_container(
            IJwtPresenter,
            JwtPresenter,
            InjectionType.SINGLETON,
        )
        presenters_container(
            IGetTokenPresenter,
            GetTokenPresenter,
            InjectionType.SINGLETON,
        )
        presenters_container(
            IUserPresenter,
            UserPresenter,
            InjectionType.SINGLETON,
        )
        presenters_container(
            ITransferCashPresenter,
            TransferCashPresenter,
            InjectionType.SINGLETON,
        )

        return presenters_container

    @classmethod
    def __create_containers(cls):
        cls.__create_use_cases_container()
        cls.__create_infrastructures_container()
        cls.__create_repositories_container()
        cls.__create_presenters_container()
        cls.__create_services_container()

    @classmethod
    def __load_containers(cls):
        WitchDoctor.load_container('use_cases')
        WitchDoctor.load_container('infrastructures')
        WitchDoctor.load_container('services')
        WitchDoctor.load_container('repositories')
        WitchDoctor.load_container('presenters')

    @classmethod
    def build_ioc_container(cls):
        cls.__create_containers()
        cls.__load_containers()
