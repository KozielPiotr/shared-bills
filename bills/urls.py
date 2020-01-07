# pylint: disable=invalid-name
"""Urls for bills application."""

from django.urls import include, path
from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter

from bills import models, serializers
from bills.views import create_nested_viewset, EventViewset


router = SimpleRouter()
router.register("events", EventViewset, basename="events")

event_router = routers.NestedSimpleRouter(router, "events", lookup="event")
event_router.register(
    "participants",
    create_nested_viewset(serializers.ParticipantSerializer, models.Participant),
    basename="participants",
)
event_router.register(
    "bills",
    create_nested_viewset(serializers.BillSerializer, models.Bill),
    basename="bills",
)
event_router.register(
    "payments",
    create_nested_viewset(serializers.PaymentSerializer, models.Payment),
    basename="payments",
)

app_name = "bills"

urlpatterns = [path("", include(router.urls)), path("", include(event_router.urls))]
