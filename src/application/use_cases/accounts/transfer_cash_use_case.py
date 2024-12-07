from loguru import logger
from witch_doctor import WitchDoctor

from src.application.data_types.dtos.jwt_dto import JwtDecodedDto
from src.application.data_types.dtos.transaction_dto import TransactionDto
from src.application.data_types.requests.accounts.transfer_request import (
    TransferCashRequest,
)
from src.application.ports.presenters.accounts.i_transfer_cash_presenter import (  # noqa: E501
    ITransferCashPresenter,
)
from src.application.ports.repositories.accounts.accounts_repository import (
    IAccountsRepository,
)
from src.application.ports.use_cases.accounts.i_transfer_cash_use_case import (
    ITransferCashUseCase,
)
from src.domain.exceptions.application.exception import (
    TransferOperationNotAllowedException,
    UnexpectedApplicationException,
)
from src.domain.exceptions.base.exception import (
    AdapterException,
    ApplicationException,
    DomainException,
    ExternalException,
)


class TransferCashUseCase(ITransferCashUseCase):
    @WitchDoctor.injection
    def __init__(
        self,
        transfer_cash_presenter: ITransferCashPresenter,
        accounts_repository: IAccountsRepository,
    ):
        self._transfer_cash_presenter = transfer_cash_presenter
        self._accounts_repository = accounts_repository

    async def transfer_cash(
        self,
        decoded_token_dto: JwtDecodedDto,
        request: TransferCashRequest,
    ) -> TransactionDto:
        try:
            if request.origin.cpf != decoded_token_dto.cpf:
                raise TransferOperationNotAllowedException()

            if request.target.account_id != decoded_token_dto.account_id:
                raise TransferOperationNotAllowedException()

            transaction_entity = self._transfer_cash_presenter.from_input_request_to_transaction_entity(  # noqa: E501
                transfer_cash_request=request
            )
            transaction_model = (
                self._transfer_cash_presenter.from_entity_to_output_model(
                    entity=transaction_entity
                )
            )
            await self._accounts_repository.update_balance(
                transaction_model=transaction_model
            )
            transaction_dto = self._transfer_cash_presenter.from_transaction_model_to_output_dto(  # noqa: E501
                model=transaction_model
            )
            return transaction_dto

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
