"""Urls for bills application."""

from django.urls import include, path
from rest_framework.routers import SimpleRouter

from accounts.views import UserCreate, UserViewset


router = SimpleRouter()
router.register("users", UserViewset, basename="users")

app_name = "accounts"

urlpatterns = [
    path("register-user/", UserCreate.as_view(), name="account-create"),
    path("users/", include(router.urls)),
]
