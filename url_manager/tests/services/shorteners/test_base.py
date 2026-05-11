from django.test import TestCase, override_settings

from url_manager.exceptions import ShortenerNotFoundException
from url_manager.services.shorteners import ShortenerProvider
from url_manager.services.shorteners.base import BaseShortener


class ExampleShortener(BaseShortener):
    def encode(self, identifier: int) -> str:
        return "TEST"


class ShortenerProviderTests(TestCase):
    def setUp(self):
        self._shortener_provider = ShortenerProvider()

    def test_get_instance(self) -> None:
        with override_settings(SHORTENER=f"{ExampleShortener.__module__}.{ExampleShortener.__name__}"):
            instance = self._shortener_provider.get_shortener_instance()
            self.assertIsInstance(instance, ExampleShortener)
        with override_settings(SHORTENER=f"INVALID.NAME"):
            with self.assertRaises(ShortenerNotFoundException):
                self._shortener_provider.get_shortener_instance()
