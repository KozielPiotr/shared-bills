# pylint: disable=redefined-builtin, unused-argument, too-many-ancestors
"""
Views for accounts application.
"""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from accounts.models import User
from accounts.serializers import RegisterUserSerializer, UserSerializer


class UserCreate(APIView):
    """View for new user registration."""

    @classmethod
    def post(cls, request, format="json"):
        """Allows POST method."""
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewset(ReadOnlyModelViewSet):
    """Viewset for User object."""

    serializer_class = UserSerializer
    queryset = User.objects.all()
