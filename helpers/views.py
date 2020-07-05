from rest_framework import permissions
from rest_framework import viewsets
from settings.permissions import IsOwnerOrReadOnly


class RestrictedView(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

