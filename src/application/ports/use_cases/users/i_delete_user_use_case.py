from abc import ABC, abstractmethod


class IDeleteUserUseCase(ABC):
    @abstractmethod
    async def delete_user(self, user_id: int):
        pass
