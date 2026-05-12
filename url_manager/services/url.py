from django.conf import settings
from django.core.cache import caches

from url_manager.exceptions import ShortUrlNotFoundException
from url_manager.models import ShortUrl


class UrlManager:
    def __init__(self,  cache_name: str | None = settings.SHORTENER_CACHE_NAME,
                 cache_ttl: int = settings.SHORTENER_CACHE_TTL):
        self._cache = None
        self._cache_ttl = cache_ttl
        if cache_name:
            self._cache = caches[cache_name]

    def get_url(self, short_name: str) -> str:
        try:
            if not self._cache:
                return ShortUrl.objects.get(short_name=short_name).url
            url = self._cache.get(short_name)
            if not url:
                url = ShortUrl.objects.get(short_name=short_name).url
                self._cache.set(short_name, url, self._cache_ttl)
            return url
        except ShortUrl.DoesNotExist as e:
            raise ShortUrlNotFoundException(f"{short_name} does not exist! {str(e)}") from e
