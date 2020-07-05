from rest_framework.generics import get_object_or_404

from helpers.views import RestrictedView
from posts.models import Post
from posts.serializer import PostSerializer
from topics.models import Topic


class PostViewSet(RestrictedView):

    serializer_class = PostSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, topic=self.get_parent())

    def get_parent(self):
        return get_object_or_404(Topic, url_name=self.kwargs.get('topic_url_name'))

    def get_queryset(self):
        return Post.objects.filter(topic=self.get_parent())
