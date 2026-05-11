from abc import ABC, abstractmethod


class BaseShortener(ABC):
    @abstractmethod
    def encode(self, identifier: int) -> str:
        pass
