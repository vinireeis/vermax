from src.application.data_types.dtos.account_dto import AccountDto
from src.application.data_types.responses.accounts.accounts_response import (
    GetBalancePayload,
    GetBalanceResponse,
)
from src.application.ports.presenters.accounts.i_get_balance_presenter import (
    IGetBalancePresenter,
)
from src.domain.models.accounts.account_model import AccountModel


class GetBalancePresenter(IGetBalancePresenter):
    @staticmethod
    def from_account_model_to_output_dto(model: AccountModel) -> AccountDto:
        dto = AccountDto(
            balance=model.balance,
            branch_id=model.branch_id,
            account_id=model.account_id,
        )
        return dto

    @staticmethod
    def from_transaction_dto_to_output_response(
        dto: AccountDto,
    ) -> GetBalanceResponse:
        payload = GetBalancePayload(
            balance=dto.balance,
        )
        response = GetBalanceResponse(
            success=True,
            payload=payload,
        )
        return response
