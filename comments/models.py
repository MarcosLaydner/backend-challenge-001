from django.db import models


class Comment(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    author = models.ForeignKey('accounts.User', related_name='comments', default=1, on_delete=models.CASCADE)
    content = models.CharField(max_length=560, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('posts.Post', related_name='comment', default=1, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
