# pylint: disable=,missing-class-docstring, too-few-public-methods
"""
Serializers for accounts application.
"""

from rest_framework.serializers import CharField, EmailField, ModelSerializer
from rest_framework.validators import UniqueValidator

from accounts.models import User


class UserSerializer(ModelSerializer):
    """Serializer for User object."""

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
        fields = ["id", "email", "password"]


class UserChangePasswordSerializer(ModelSerializer):
    """Serializer for password change."""

    old_password = CharField(write_only=True, required=True)
    new_password = CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ["old_password", "new_password"]


class UserDeleteSerializer(ModelSerializer):
    """Serializer for User removal."""

    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["password"]
