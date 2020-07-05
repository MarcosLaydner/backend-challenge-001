from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ['title', 'author', 'created_at', 'updated_at', 'content', 'post', 'id']