"""Urls for bills application."""

from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView
from rest_framework.routers import DynamicRoute, Route, SimpleRouter

from accounts.views import UserViewset


class UserRouter(SimpleRouter):
    """Customised router for User object"""

    routes = [
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={"get": "retrieve"},
            name="{basename}-detail",
            detail=True,
            initkwargs={"suffix": "Instance"},
        ),
        DynamicRoute(
            url=r"^{prefix}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=True,
            initkwargs={},
        ),
    ]


router = UserRouter()
router.register("user", UserViewset, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("verify-token/", TokenVerifyView.as_view(), name="token-verify"),
]
