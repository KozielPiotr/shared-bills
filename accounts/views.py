# pylint: disable=unused-argument, too-many-ancestors
"""Views for accounts application."""

from django.contrib.auth import get_user
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated
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
        return get_user(self.request)

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

    @action(detail=True, methods=["patch"], permission_classes=[IsAuthenticated])
    def change_data(self, request, *args, **kwargs):
        """Changes user data."""

        serializer = UserSerializer(
            instance=self.get_object(), data=request.data, context={"request": request}
        )
        serializer.Meta.fields = ["email", "password"]
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
