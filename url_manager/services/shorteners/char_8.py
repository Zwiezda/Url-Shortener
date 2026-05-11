import logging

from django.conf import settings
from hashids import Hashids

from .base import BaseShortener

logger = logging.getLogger(__name__)


class Char8Shortener(BaseShortener):
    def __init__(self, hash_ids: Hashids | None = None):
        self._hash_ids = hash_ids or Hashids(salt=settings.SECRET_KEY, min_length=8)

    def encode(self, identifier: int) -> str:
        encoded_id = self._hash_ids.encode(identifier)
        logger.debug(f"Encoding {identifier} to {encoded_id}")
        return encoded_id
