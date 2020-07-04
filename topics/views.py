from helpers.views import CommonView
from topics.models import Topic
from topics.serializer import TopicSerializer


class TopicViewSet(CommonView):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'url_name'

