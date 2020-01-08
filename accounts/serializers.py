# pylint: disable=,missing-class-docstring, too-few-public-methods
"""
Serializers for accounts application.
"""

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    HyperlinkedIdentityField,
)
from rest_framework.validators import UniqueValidator

from accounts.models import User


class UserSerializer(ModelSerializer):
    """Serializer for User object."""

    url = HyperlinkedIdentityField(view_name="accounts:users-detail")
    email = EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        """Creates User object."""

        user = User.objects.create_user(
            validated_data["email"], validated_data["password"]
        )
        return user

    class Meta:
        model = User
        fields = ["id", "url", "email", "password"]
