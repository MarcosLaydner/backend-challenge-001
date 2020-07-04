from rest_framework import serializers
from topics.models import Topic


class TopicSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Topic
        fields = ['title', 'author','created_at', 'updated_at', 'name', 'description', 'url_name']
        lookup_field = 'url_name'
