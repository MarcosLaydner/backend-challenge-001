from rest_framework import serializers

from comments.serializer import CommentSerializer
from posts.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    topic = serializers.ReadOnlyField(source='topic.url_name')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'created_at', 'updated_at', 'topic', 'comments', 'id']
        lookup_field = 'pk'
