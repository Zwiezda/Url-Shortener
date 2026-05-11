from rest_framework.exceptions import NotFound


class ShortenerNotFoundException(Exception):
    pass


class ShortUrlNotFoundException(NotFound):
    pass
