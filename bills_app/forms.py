# pylint: disable=too-few-public-methods, missing-class-docstring
"""Forms for bills_app."""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Create CustomUser."""

    class Meta:
        model = CustomUser
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    """Change CustomUser."""

    class Meta:
        model = CustomUser
        fields = ("username",)
