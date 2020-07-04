from django.db import models
from helpers.models import CommonInfo


class Topic(CommonInfo):
    name = models.CharField(max_length=32, default='')
    description = models.CharField(max_length=128, blank=True, default='')
    url_name = models.SlugField(max_length=24, default='')

    class Meta:
        ordering = ['created_at']
