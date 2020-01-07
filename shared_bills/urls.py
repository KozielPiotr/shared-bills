"""shared_bills URL Configuration"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import APIRootView


api_root_views = {
    "events": "bills:events-list",
    "register user": "accounts:account-create",
    "users": "accounts:users-list",
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", APIRootView.as_view(api_root_dict=api_root_views), name="api-root"),
    path("api/", include("bills.urls")),
    path("api/", include("accounts.urls")),
]
