from rest_framework import permissions
from rest_framework import viewsets

from comments.models import Comment
from posts.serializer import CommentSerializer
from settings.permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Comment.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
