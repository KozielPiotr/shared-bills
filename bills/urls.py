# pylint: disable=invalid-name
"""Urls for bills application"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from bills import models, serializers
from bills.views import create_viewset


router = DefaultRouter()
router.register(
    "participants",
    create_viewset(serializers.ParticipantSerializer, models.Participant, False),
)

router.register(
    "events", create_viewset(serializers.EventSerializer, models.Event, False)
)
event_router = NestedSimpleRouter(router, "events", lookup="event")
event_router.register(
    "participants",
    create_viewset(serializers.ParticipantSerializer, models.Participant, True),
    base_name="event-participants",
)
event_router.register(
    "bills",
    create_viewset(serializers.BillSerializer, models.Bill, True),
    base_name="event-bills",
)
event_router.register(
    "payments",
    create_viewset(serializers.PaymentSerializer, models.Payment, True),
    base_name="event-payments",
)

router.register("bills", create_viewset(serializers.BillSerializer, models.Bill, False))
router.register(
    "payments", create_viewset(serializers.PaymentSerializer, models.Payment, False)
)

urlpatterns = [path("", include(router.urls)), path("", include(event_router.urls))]
