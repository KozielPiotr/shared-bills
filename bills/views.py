# pylint: disable=too-many-ancestors,no-member, unused-argument
"""Views for bills application."""

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated

from .models import Event
from .serializers import EventSerializer, EventRetrieveSerializer


class IsOwner(BasePermission):
    """Only user related to object can have access to it."""

    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)


def create_nested_viewset(serializer_obj, model):
    """
    Creates viewsets for objects related to the Event object
    :param serializer_obj: serializer class
    :param model: database model
    :return: new viewset class
    """

    class RelationshipViewset(viewsets.ModelViewSet):
        """Viewsets for objects related to the Event object."""

        def __init__(self, *args, **kwargs):
            self.__class__.__name__ = "{}".format(model.__name__)
            super().__init__(*args, **kwargs)

        serializer_class = serializer_obj
        permission_classes = [IsAuthenticated]

        def get_user(self):
            """returns current user."""

            return self.request.user

        def get_queryset(self):
            """Query of all Participant objects being related to the given Event."""

            return model.objects.filter(event=self.get_event())

        def get_event(self):
            """Gets queryset for Event objects with given pk."""

            query = Event.objects.filter(
                pk=self.kwargs["event_pk"], user=self.request.user
            )
            return get_object_or_404(query)

    return RelationshipViewset


class EventViewset(viewsets.ModelViewSet):
    """Viewset for non-nested objects."""

    permission_classes = [IsOwner, IsAuthenticated]

    def get_user(self):
        """returns current user."""

        return self.request.user

    def get_queryset(self):
        return Event.objects.filter(user=self.get_user())

    def get_serializer_class(self):
        if self.action == "retrieve":
            return EventRetrieveSerializer
        return EventSerializer
