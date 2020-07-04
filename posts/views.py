from helpers.views import CommonView
from posts.models import Post
from posts.serializer import PostSerializer


class PostViewSet(CommonView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

