from abc import ABC, abstractmethod

from src.application.data_types.dtos.transaction_dto import TransactionDto
from src.application.data_types.requests.accounts.transfer_request import (
    TransferCashRequest,
)
from src.application.data_types.responses.accounts.accounts_response import (
    TransferCashResponse,
)
from src.domain.entities.transaction_entity import TransactionEntity
from src.domain.models.transactions.transaction_model import TransactionModel


class ITransferCashPresenter(ABC):
    @staticmethod
    @abstractmethod
    def from_input_request_to_transaction_entity(
        transfer_cash_request: TransferCashRequest,
    ) -> TransactionEntity:
        pass

    @staticmethod
    @abstractmethod
    def from_entity_to_output_model(
        entity: TransactionEntity,
    ) -> TransactionModel:
        pass

    @staticmethod
    @abstractmethod
    def from_transaction_model_to_output_dto(
        model: TransactionModel,
    ) -> TransactionDto:
        pass

    @staticmethod
    @abstractmethod
    def from_transaction_dto_to_output_response(
        dto: TransactionDto,
    ) -> TransferCashResponse:
        pass
