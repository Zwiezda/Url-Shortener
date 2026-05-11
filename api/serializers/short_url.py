from rest_framework import serializers

from url_manager.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.HyperlinkedIdentityField(view_name='short-url-go', read_only=True, lookup_field='short_name')

    class Meta:
        model = ShortUrl
        read_only_fields = ('short_name', 'created_at')
        fields = ('short_name', 'url', 'created_at', 'short_url')
