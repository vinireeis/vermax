from src.application.data_types.dtos.transaction_dto import TransactionDto
from src.application.data_types.requests.accounts.transfer_request import (
    TransferCashRequest,
)
from src.application.data_types.responses.accounts.accounts_response import (
    TransferCashResponse,
    TransferPayload,
)
from src.application.ports.presenters.accounts.i_transfer_cash_presenter import (  # noqa: E501
    ITransferCashPresenter,
)
from src.domain.entities.transaction_entity import TransactionEntity
from src.domain.exceptions.adapters.exception import (
    UnexpectedPresenterException,
)
from src.domain.models.transactions.enums.transactions_enum import (
    TransactionOperationEnum,
)
from src.domain.models.transactions.transaction_model import TransactionModel


class TransferCashPresenter(ITransferCashPresenter):
    @staticmethod
    def from_input_request_to_transaction_entity(
        transfer_cash_request: TransferCashRequest,
    ) -> TransactionEntity:
        try:
            entity = TransactionEntity(
                amount=transfer_cash_request.amount,
                account_id=transfer_cash_request.target.account_id,
                transaction_operation=TransactionOperationEnum.TRANSFER,
            )
            return entity

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_entity_to_output_model(
        entity: TransactionEntity,
    ) -> TransactionModel:
        try:
            model = TransactionModel(
                account_id=entity.account_id,
                amount=entity.amount,
                transaction_operation=entity.transaction_operation,
                transaction_id=entity.transaction_id,
            )
            return model

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_transaction_model_to_output_dto(
        model: TransactionModel,
    ) -> TransactionDto:
        try:
            dto = TransactionDto(
                transaction_id=model.transaction_id,
                account_id=model.account_id,
                amount=model.amount,
                operation=model.transaction_operation,
                created_at=model.created_at,
            )
            return dto

        except Exception as ex:
            raise UnexpectedPresenterException(original_error=ex)

    @staticmethod
    def from_transaction_dto_to_output_response(
        dto: TransactionDto,
    ) -> TransferCashResponse:
        payload = TransferPayload(
            transaction_id=dto.transaction_id,
            account_id=dto.account_id,
            amount=dto.amount,
            operation=dto.operation,
            created_at=dto.created_at,
        )
        response = TransferCashResponse(
            success=True,
            message='Transferred with successfully',
            payload=payload,
        )
        return response
