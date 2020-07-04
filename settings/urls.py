"""
backend-challenge-001 URL Configuration
"""
###
# Libraries
###
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested import routers
from topics.views import TopicViewSet
from posts.views import PostViewSet
from comments.views import CommentViewSet

from helpers.health_check_view import health_check

###
# URLs
###

router = routers.SimpleRouter()
router.register(r'topics', TopicViewSet)

topics_router = routers.NestedSimpleRouter(router, r'topics', lookup='topic')
topics_router.register(r'posts', PostViewSet, basename='posts')

posts_router = routers.NestedSimpleRouter(topics_router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),
    url(r'api-auth/', include('rest_framework.urls')),

    # Health Check
    url(r'health-check/$', health_check, name='health_check'),

    # Applications
    url(r'^', include('accounts.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include(router.urls)),
    url(r'^', include(topics_router.urls)),
    url(r'^', include(posts_router.urls)),
]
