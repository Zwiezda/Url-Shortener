from hashids import Hashids

from shorteners.base import BaseShortener


class Char8Shortener(BaseShortener):
    def __init__(self):
        self._hash_ids = Hashids(salt=, min_length=8)

    def encode(self, identifier: int) -> str:
        pass