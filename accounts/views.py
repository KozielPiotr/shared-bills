# pylint: disable=unused-argument, too-many-ancestors
"""Views for accounts application."""

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.models import User
from accounts.serializers import UserSerializer


class UserViewset(ModelViewSet):
    """Viewset for User object."""

    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=["post"], url_path="register", url_name="register")
    def register_user(self, request, *args, **kwargs):
        """Registering new User."""

        # todo Should be only available for anonymous user.
        serializer = UserSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=False, methods=["get", "post"], url_path="register", url_name="register")
    # def edit_user(self, request, *args, **kwargs):
    #     """Registering new User."""
    #
    #     # todo Should be only available for anonymous user.
    #     serializer = UserSerializer(data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         if user:
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
