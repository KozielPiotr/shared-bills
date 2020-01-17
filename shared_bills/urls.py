# pylint: disable=invalid-name
"""shared_bills URL Configuration"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import APIRootView


api_root_views = {
    "events": "events-list",
    "user": "user-detail",
    "get token": "token_obtain_pair",
    "verify token": "token_verify",
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", APIRootView.as_view(api_root_dict=api_root_views), name="api-root"),
    path("api/", include("bills.urls")),
    path("api/", include("accounts.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("auth/", include("rest_framework.urls")))
