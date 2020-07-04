from comments.models import Comment
from comments.serializer import CommentSerializer
from helpers.views import CommonView


class CommentViewSet(CommonView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
