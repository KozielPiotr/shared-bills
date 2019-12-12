"""Urls for bills application"""

from django.urls import include, path
from rest_framework import routers

from bills import views


router = routers.DefaultRouter()
router.register("participants", views.ParticipantViewset)
router.register("events", views.EventViewset)
router.register("bills", views.BillViewset)
router.register("payments", views.PaymentViewset)

urlpatterns = [path("", include(router.urls))]
