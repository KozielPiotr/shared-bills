# pylint: disable=too-many-ancestors,no-member, unused-argument
"""Views for bills application."""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from bills import models, serializers


class ParticipantViewset(viewsets.ModelViewSet):
    """Participant viewset"""

    queryset = models.Participant.objects.all()
    serializer_class = serializers.ParticipantSerializer


class EventViewset(viewsets.ModelViewSet):
    """Event viewset"""

    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    @action(detail=True, methods=["GET"])
    def event_participants(self, request, *args, **kwargs):
        """Returns all participants related to the event"""
        event = self.get_object()
        queryset = event.participants.all()
        serializer = serializers.ParticipantSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)


class BillViewset(viewsets.ModelViewSet):
    """Bill viewset"""

    queryset = models.Bill.objects.all()
    serializer_class = serializers.BillSerializer


class PaymentViewset(viewsets.ModelViewSet):
    """Bill viewset"""

    queryset = models.Payment.objects.all()
    serializer_class = serializers.PaymentSerializer
