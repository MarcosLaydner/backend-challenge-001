from rest_framework.generics import get_object_or_404

from comments.models import Comment
from comments.serializer import CommentSerializer
from helpers.views import RestrictedView
from posts.models import Post


class CommentViewSet(RestrictedView):

    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_parent())

    def get_parent(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_pk'))

    def get_queryset(self):
        return Comment.objects.filter(post=self.get_parent())