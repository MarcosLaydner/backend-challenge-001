from rest_framework import serializers
from topics.models import Topic


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Topic
        fields = ['name', 'title', 'author', 'url_name', 'created_at', 'updated_at']
