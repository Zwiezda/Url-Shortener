from unittest.mock import MagicMock

from django.test import TestCase

from url_manager.services.shorteners import Char8Shortener


class ShortenerProviderTests(TestCase):
    def setUp(self):
        self._snowflake_generator = MagicMock()
        self._hash_ids = MagicMock()
        self._shortener = Char8Shortener(self._hash_ids, self._snowflake_generator)

    def test_encode(self) -> None:
        self._snowflake_generator.__next__.return_value = 1234
        self._hash_ids.encode.side_effect = lambda snowflake_id: "CORRECT_ID" if snowflake_id == 1234 else "ERROR"
        self.assertEqual('CORRECT_ID', self._shortener.encode("test_url"))
