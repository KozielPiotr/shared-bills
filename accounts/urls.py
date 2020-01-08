"""Urls for bills application."""

from django.urls import include, path
from rest_framework.routers import DynamicRoute, Route, SimpleRouter

from accounts.views import UserViewset


class UserRouter(SimpleRouter):
    """Customised router for User object"""

    routes = [
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            },
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

# app_name = "accounts"

urlpatterns = [path("", include(router.urls))]
