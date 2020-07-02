from accounts import models
from rest_framework import viewsets

from users.serializer import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
