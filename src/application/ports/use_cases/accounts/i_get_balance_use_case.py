from abc import ABC, abstractmethod

from src.application.data_types.dtos.account_dto import AccountDto
from src.application.data_types.dtos.jwt_dto import JwtDecodedDto


class IGetBalanceUseCase(ABC):
    @abstractmethod
    async def get_user_balance(
        self, decoded_token_dto: JwtDecodedDto
    ) -> AccountDto:
        pass
