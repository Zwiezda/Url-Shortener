from django.db import models
from django.utils import timezone


class ShortUrl(models.Model):
    short_name = models.SlugField(unique=True, null=True)
    url = models.URLField()
    created_at = models.DateTimeField(verbose_name='Created at', default=timezone.now)

    def __str__(self) -> str:
        return f"{self.short_name} - {self.url}"

    def save(self, *, force_insert=False, force_update=False, using=None, update_fields=None):
        result = super().save(force_insert=force_insert, force_update=force_update,
                              using=using, update_fields=update_fields)
        if not self.short_name:
            from url_manager.services.shorteners import ShortenerProvider
            shortener = ShortenerProvider().get_shortener_instance()
            self.short_name = shortener.encode(self.id)
            self.save()
        return result
