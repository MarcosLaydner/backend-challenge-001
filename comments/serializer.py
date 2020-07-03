from rest_framework import serializers
from topics.models import Topic


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username', related_name='comment_author')

    class Meta:
        model = Topic
        fields = ['title', 'author', 'content', 'created_at', 'updated_at', 'post']