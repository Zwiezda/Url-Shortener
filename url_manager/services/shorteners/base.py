import importlib
from abc import ABC, abstractmethod

from django.conf import settings

from url_manager.exceptions import ShortenerNotFoundException


class BaseShortener(ABC):
    @abstractmethod
    def encode(self, identifier: int) -> str:
        pass


class ShortenerProvider:
    def get_shortener_instance(self) -> BaseShortener:
        try:
            module_name, class_name = settings.SHORTENER.rsplit(".", 1)
            return getattr(importlib.import_module(module_name), class_name)()
        except Exception as e:
            raise ShortenerNotFoundException(f"Shortener class {settings.SHORTENER} not found: {str(e)}") from e
