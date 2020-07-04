from rest_framework import permissions
from rest_framework import viewsets
from settings.permissions import IsOwnerOrReadOnly


class CommonView(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

