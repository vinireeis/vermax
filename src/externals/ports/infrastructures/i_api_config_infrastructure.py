from abc import ABC, abstractmethod

from fastapi import FastAPI


class IApiConfigInfrastructure(ABC):
    @abstractmethod
    def start_app(self) -> FastAPI:
        pass
