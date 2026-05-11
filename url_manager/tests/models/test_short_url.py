from unittest.mock import patch, MagicMock

from django.test import TestCase

from url_manager.models import ShortUrl


class ShortUrlTests(TestCase):
    def test_save(self) -> None:
        shortener_mock = MagicMock()
        shortener_mock.encode.return_value = "test1234"
        with patch("url_manager.services.shorteners.ShortenerProvider.get_shortener_instance", return_value=shortener_mock):
            instance = ShortUrl(url="https://test.com")
            instance.save()
            self.assertEqual(shortener_mock.encode.call_count, 1)
            self.assertEqual('test1234', instance.short_name)
