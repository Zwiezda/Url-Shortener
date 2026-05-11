from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views.short_url import ShortUrlViewSet

router = DefaultRouter()
router.register('short-url', ShortUrlViewSet, basename='short-url')

urlpatterns = [
    path('go/<str:short_name>/', ShortUrlViewSet.as_view({"get": "go"}), name='short-url-go'),
] + router.urls
