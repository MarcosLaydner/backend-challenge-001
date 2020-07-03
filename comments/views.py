from rest_framework import permissions
from rest_framework import viewsets

from comments.models import Comment
from comments.serializer import CommentSerializer
from settings.permissions import IsOwnerOrReadOnly


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
