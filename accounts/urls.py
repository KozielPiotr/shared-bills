"""Urls for bills application."""

from django.urls import include, path
from rest_framework.routers import DynamicRoute, Route, SimpleRouter

from accounts.views import UserViewset


class UserRouter(SimpleRouter):
    """Customised router for User object"""

    routes = [
        # read-only route for list
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={"get": "list"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        # detail should be protected
        Route(
            url=r"^{prefix}/{lookup}/detail{trailing_slash}$",
            mapping={"get": "retrieve"},
            name="{basename}-detail",
            detail=True,
            initkwargs={"suffix": "Instance"},
        ),
        # for user registration
        DynamicRoute(
            url=r"^{prefix}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=False,
            initkwargs={},
        ),
        # for editing user
        DynamicRoute(
            url=r"^{prefix}/{lookup}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=True,
            initkwargs={},
        ),
    ]


router = UserRouter()
router.register("users", UserViewset, basename="users")

app_name = "accounts"

urlpatterns = [path("", include(router.urls))]
