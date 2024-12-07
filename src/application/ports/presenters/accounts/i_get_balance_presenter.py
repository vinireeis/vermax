from abc import ABC, abstractmethod

from src.application.data_types.dtos.account_dto import AccountDto
from src.application.data_types.responses.accounts.accounts_response import (
    GetBalanceResponse,
)
from src.domain.models.accounts.account_model import AccountModel


class IGetBalancePresenter(ABC):
    @staticmethod
    @abstractmethod
    def from_account_model_to_output_dto(model: AccountModel) -> AccountDto:
        pass

    @staticmethod
    @abstractmethod
    def from_transaction_dto_to_output_response(
        dto: AccountDto,
    ) -> GetBalanceResponse:
        pass
