# pylint: disable=invalid-name
"""Urls for bills application"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from bills import models, serializers
from bills.views import create_nested_viewset, create_viewset


router = DefaultRouter()
router.register(
    "participants",
    create_viewset(serializers.ParticipantSerializer, models.Participant),
)

router.register("events", create_viewset(serializers.EventSerializer, models.Event))
event_router = NestedSimpleRouter(router, "events", lookup="event")
event_router.register(
    "participants",
    create_nested_viewset(serializers.ParticipantNestedSerializer, models.Participant),
    basename="event-participants",
)
event_router.register(
    "bills",
    create_nested_viewset(serializers.BillNestedSerializer, models.Bill),
    basename="event-bills",
)
event_router.register(
    "payments",
    create_nested_viewset(serializers.PaymentSerializer, models.Payment),
    basename="event-payments",
)

router.register("bills", create_viewset(serializers.BillSerializer, models.Bill))
router.register(
    "payments", create_viewset(serializers.PaymentSerializer, models.Payment)
)

# app_name = "bills"
urlpatterns = [path("", include(router.urls)), path("", include(event_router.urls))]
