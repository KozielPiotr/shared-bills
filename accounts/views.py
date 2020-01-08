# pylint: disable=unused-argument, too-many-ancestors
"""Views for accounts application."""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.models import User
from accounts.serializers import UserSerializer


class IsAnonymous(BasePermission):
    """Allows access only to anonymous users."""

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)


class UserViewset(GenericViewSet, DestroyModelMixin, RetrieveModelMixin):
    """Viewset for User object."""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        return self.request.user

    @classmethod
    @action(detail=True, methods=["post"], permission_classes=[IsAnonymous])
    def register(cls, request, *args, **kwargs):
        """Registering new User."""

        serializer = UserSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
