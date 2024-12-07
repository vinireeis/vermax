from loguru import logger
from witch_doctor import WitchDoctor

from src.application.data_types.dtos.account_dto import AccountDto
from src.application.data_types.dtos.jwt_dto import JwtDecodedDto
from src.application.ports.presenters.accounts.i_get_balance_presenter import (
    IGetBalancePresenter,
)
from src.application.ports.repositories.accounts.accounts_repository import (
    IAccountsRepository,
)
from src.application.ports.use_cases.accounts.i_get_balance_use_case import (
    IGetBalanceUseCase,
)
from src.domain.exceptions.application.exception import (
    UnexpectedApplicationException,
)
from src.domain.exceptions.base.exception import (
    AdapterException,
    ApplicationException,
    DomainException,
    ExternalException,
)


class GetBalanceUseCase(IGetBalanceUseCase):
    @WitchDoctor.injection
    def __init__(
        self,
        get_balance_presenter: IGetBalancePresenter,
        accounts_repository: IAccountsRepository,
    ):
        self._get_balance_presenter = get_balance_presenter
        self._accounts_repository = accounts_repository

    async def get_user_balance(
        self, decoded_token_dto: JwtDecodedDto
    ) -> AccountDto:
        try:
            account_model = await self._accounts_repository.get_user_account(
                account_id=decoded_token_dto.account_id
            )
            account_dto = (
                self._get_balance_presenter.from_account_model_to_output_dto(
                    model=account_model
                )
            )
            return account_dto

        except (
            AdapterException,
            DomainException,
            ExternalException,
            ApplicationException,
        ) as ex:
            raise ex

        except Exception as ex:
            logger.info(ex)
            raise UnexpectedApplicationException(original_error=ex)
