# pylint: disable=unused-argument, too-many-ancestors
"""Views for accounts application."""

from django.contrib.auth import get_user
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from accounts.models import User
from accounts.serializers import (
    UserChangePasswordSerializer,
    UserDeleteSerializer,
    UserSerializer,
)


class IsAnonymous(BasePermission):
    """Allows access only to anonymous users."""

    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)


class UserViewset(GenericViewSet, RetrieveModelMixin):
    """Viewset for User object."""

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "register":
            return UserSerializer
        if self.action == "change_password":
            return UserChangePasswordSerializer
        if self.action == "delete_user":
            return UserDeleteSerializer

        return UserSerializer

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
    def change_password(self, request, *args, **kwargs):
        """Changes password."""

        user = self.get_object()
        serializer = UserChangePasswordSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            if not user.check_password(request.data.get("old_password")):
                return Response(
                    {"old_password": "wrong password"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(request.data.get("new_password"))
            user.save()
            return Response({"status": "password set"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def delete_user(self, request, *args, **kwargs):
        """Deletes user."""

        user = self.get_object()
        serializer = UserDeleteSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            if not user.check_password(request.data.get("password")):
                return Response(
                    {"password": "wrong password"}, status=status.HTTP_400_BAD_REQUEST
                )
            user.delete()
            return Response(
                {"status": "user {} deleted".format(user.email)},
                status=status.HTTP_204_NO_CONTENT,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
