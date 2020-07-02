from rest_framework import serializers
from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ['name', 'title', 'author', 'url_name', 'created_at', 'updated_at']
