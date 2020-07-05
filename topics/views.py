from helpers.views import RestrictedView
from topics.models import Topic
from topics.serializer import TopicSerializer


class TopicViewSet(RestrictedView):

    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    lookup_field = 'url_name'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

