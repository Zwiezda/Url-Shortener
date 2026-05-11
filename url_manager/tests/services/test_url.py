from django.test import TestCase, override_settings

from url_manager.exceptions import ShortUrlNotFoundException
from url_manager.models import ShortUrl
from url_manager.services import UrlManager
from django.core.cache import caches


TEST_CACHE_NAME = 'test-cache'

@override_settings(CACHES={
    TEST_CACHE_NAME: {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
})
class UrlManagerTests(TestCase):
    fixtures = [
        'fixtures/short_url.json',
    ]

    def setUp(self):
        self._cache_manager = UrlManager(TEST_CACHE_NAME, 3600)
        self._no_cache_manager = UrlManager(None)

    def test_get_url_with_cache(self) -> None:
        short_url = ShortUrl.objects.first()
        url = self._cache_manager.get_url(short_url.short_name)
        self.assertEqual(short_url.url, url)
        self.assertEqual(short_url.url, caches[TEST_CACHE_NAME].get(short_url.short_name))
        with self.assertRaises(ShortUrlNotFoundException):
            self._cache_manager.get_url("INVALID_NAME")

    def test_get_url_without_cache(self) -> None:
        short_url = ShortUrl.objects.first()
        url = self._no_cache_manager.get_url(short_url.short_name)
        self.assertEqual(short_url.url, url)
        self.assertIsNone(caches[TEST_CACHE_NAME].get(short_url.short_name))
        with self.assertRaises(ShortUrlNotFoundException):
            self._cache_manager.get_url("INVALID_NAME")

    def tearDown(self):
        caches[TEST_CACHE_NAME].clear()