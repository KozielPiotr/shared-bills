# pylint: disable=too-many-ancestors,no-member
"""Views for bills application."""

from rest_framework import viewsets

from bills import models, serializers


class ParticipantViewset(viewsets.ModelViewSet):
    """Participant viewset"""

    queryset = models.Participant.objects.all()
    serializer_class = serializers.ParticipantSerializer


class EventViewset(viewsets.ModelViewSet):
    """Event viewset"""

    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class BillViewset(viewsets.ModelViewSet):
    """Bill viewset"""

    queryset = models.Bill.objects.all()
    serializer_class = serializers.BillSerializer


class PaymentViewset(viewsets.ModelViewSet):
    """Bill viewset"""

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
