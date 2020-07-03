"""
Model helper
"""
###
# Libraries
###
from django.db import models


###
# Helpers
###
class TimestampModel(models.Model):
    '''
        Extend this model if you wish to have automatically updated
        created_at and updated_at fields.
    '''

    class Meta:
        abstract = True

    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)


class CommonInfo(models.Model):
    title = models.CharField(max_length=64, blank=True, default='')
    author = models.ForeignKey('accounts.User', related_name='comments', default=1, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True