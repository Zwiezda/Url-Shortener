from django.db import models

class ShortUrl(models.Model):
    short_name = models.SlugField(unique=True)
    url = models.URLField()
