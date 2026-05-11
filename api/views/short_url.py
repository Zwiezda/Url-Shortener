from django.http import HttpResponseRedirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.serializers import ShortUrlSerializer
from url_manager.models import ShortUrl
from url_manager.services import UrlManager


class ShortUrlViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = ShortUrl.objects.all()
    serializer_class = ShortUrlSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    lookup_field = 'short_name'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._url_manager = None

    def go(self, request: Request, short_name: str | None = None) -> Response | HttpResponseRedirect:
        url_manager = self._get_url_manager()
        url = url_manager.get_url(short_name)
        return HttpResponseRedirect(url)

    def _get_url_manager(self) -> UrlManager:
        if self._url_manager is None:
            self._url_manager = UrlManager()
        return self._url_manager
