from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=32, default='')
    title = models.CharField(max_length=64, blank=True, default='')
    author = models.ForeignKey('accounts.User', related_name='topics', default=1, on_delete=models.CASCADE)
    description = models.CharField(max_length=128, blank=True, default='')
    url_name = models.CharField(max_length=24, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
