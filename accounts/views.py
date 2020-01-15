# pylint: disable=unused-argument, too-many-ancestors
"""Views for accounts application."""

from django.contrib.auth import get_user
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.models import User
from accounts.serializers import (
    PasswordCheckSerializer,
    UserChangePasswordSerializer,
    UserSerializer,
)


class IsAnonymous(BasePermission):
    """Allows access only to anonymous users."""

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)


class UserViewset(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    """Viewset for User object."""

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "register":
            return UserSerializer
        if self.action == "change_password":
            return UserChangePasswordSerializer
        if self.action == "delete_user":
            return PasswordCheckSerializer

        return UserSerializer

    def get_object(self):
        return get_user(self.request)

    @action(detail=True, methods=["post"], permission_classes=[IsAnonymous])
    def register(self, request, *args, **kwargs):
        """Registering new User."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def change_password(self, request, *args, **kwargs):
        """Changes password."""
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "password changed"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def delete_user(self, request, *args, **kwargs):
        """Deletes user."""
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        user.delete()
        return Response({"detail": "user deleted"}, status=status.HTTP_200_OK)
