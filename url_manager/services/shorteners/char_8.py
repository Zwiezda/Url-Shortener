import logging

from django.conf import settings
from hashids import Hashids
from snowflake import SnowflakeGenerator

from .base import BaseShortener

logger = logging.getLogger(__name__)


class Char8Shortener(BaseShortener):
    def __init__(self, hash_ids: Hashids | None = None, snowflake_generator: SnowflakeGenerator | None = None,):
        self._hash_ids = hash_ids or Hashids(salt=settings.SECRET_KEY, min_length=8)
        self._snowflake_generator = snowflake_generator or SnowflakeGenerator(1)

    def encode(self, url: str) -> str:
        encoded_id = next(self._snowflake_generator)
        encoded_id = self._hash_ids.encode(encoded_id)
        logger.debug(f"Encoding {url} to {encoded_id}")
        return encoded_id
