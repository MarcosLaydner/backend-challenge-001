from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    topic = serializers.ReadOnlyField(source='topic.title')

    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'created_at', 'updated_at', 'topic']