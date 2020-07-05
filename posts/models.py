from django.db import models

from helpers.models import CommonInfo


class Post(CommonInfo):
    content = models.CharField(max_length=1024, blank=True, default='')
    topic = models.ForeignKey('topics.Topic', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
