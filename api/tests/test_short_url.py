from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from url_manager.models import ShortUrl


class ShortUrlViewSetTests(APITestCase):
    fixtures = [
        'fixtures/short_url.json',
    ]

    def test_list_short_urls(self) -> None:
        response = self.client.get(reverse('short-url-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ShortUrl.objects.count(), response.data['count'])

    def test_get_short_url(self) -> None:
        short_url = ShortUrl.objects.first()
        response = self.client.get(reverse('short-url-detail', args=[short_url.short_name]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(short_url.url, response.data['url'])
        response = self.client.get(reverse('short-url-detail', args=['INVALID_CODE']))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_short_url(self) -> None:
        new_url = 'http://example.com/test123455/'
        response = self.client.post(reverse('short-url-list'), data={'url': new_url}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['short_name'])
        self.assertIsNotNone(response.data['short_url'])
        self.assertEqual(new_url, response.data['url'])
        response = self.client.post(reverse('short-url-list'), data={'url': 'INVALID-URL'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_redirect_short_url(self) -> None:
        short_url = ShortUrl.objects.first()
        response = self.client.get(reverse('short-url-go', args=[short_url.short_name]))
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.headers['Location'], short_url.url)
        response = self.client.get(reverse('short-url-go', args=['INVALID_CODE']))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_short_url(self) -> None:
        short_url = ShortUrl.objects.first()
        response = self.client.delete(reverse('short-url-detail', args=[short_url.short_name]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_full_path(self) -> None:
        new_url = 'http://example.com/test123455/'
        response = self.client.post('/api/short-url/', data={'url': new_url}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(response.data['short_url'])
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.headers['Location'], new_url)
