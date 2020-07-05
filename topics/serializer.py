from rest_framework import serializers

from posts.serializer import PostSerializer
from topics.models import Topic


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ['title', 'author','created_at', 'updated_at', 'name', 'description', 'url_name', 'posts']
        lookup_field = 'url_name'
