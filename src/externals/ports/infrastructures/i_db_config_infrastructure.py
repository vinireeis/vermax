from abc import ABC, abstractmethod
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession


class IDbConfigInfrastructure(ABC):
    @classmethod
    @abstractmethod
    def get_session(cls) -> AsyncGenerator[AsyncSession, None]:
        pass
