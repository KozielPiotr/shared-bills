# pylint: disable=,missing-class-docstring, too-few-public-methods
"""
Serializers for accounts application.
"""

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
)
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


class PasswordCheckSerializer(ModelSerializer):
    """Checks if given password is valid."""

    password = CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["password"]

    def validate_password(self, value):
        """Raises ValidationError if password is invalid."""
        if not self.instance.check_password(value):
            raise ValidationError("Wrong password")


class UserChangePasswordSerializer(PasswordCheckSerializer):
    """Serializer for password change."""

    new_password = CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ["password", "new_password"]

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance
