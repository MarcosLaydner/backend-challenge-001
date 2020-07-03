from django.db import models
from helpers.models import CommonInfo


class Comment(CommonInfo):
    content = models.CharField(max_length=560, blank=True, default='')
    post = models.ForeignKey('posts.Post', related_name='comments', default=1, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
