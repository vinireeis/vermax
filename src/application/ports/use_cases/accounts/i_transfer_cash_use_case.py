from abc import ABC, abstractmethod

from src.application.data_types.dtos.jwt_dto import JwtDecodedDto
from src.application.data_types.dtos.transaction_dto import TransactionDto
from src.application.data_types.requests.accounts.transfer_request import (
    TransferCashRequest,
)


class ITransferCashUseCase(ABC):
    @abstractmethod
    async def transfer_cash(
        self, decoded_token_dto: JwtDecodedDto, request: TransferCashRequest
    ) -> TransactionDto:
        pass
