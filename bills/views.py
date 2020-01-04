# pylint: disable=too-many-ancestors,no-member, unused-argument
"""Views for bills application."""

from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import Event


def create_nested_viewset(serializer_obj, model):
    """
    Creates viewsets for objects related to the Event object
    :param serializer_obj: serializer class
    :param model: database model
    :return: new viewset class
    """

    class RelationshipViewset(viewsets.ModelViewSet):
        """Viewsets for objects related to the Event object"""

        def __init__(self, *args, **kwargs):
            self.__class__.__name__ = "{}".format(model.__name__)
            super().__init__(*args, **kwargs)

        serializer_class = serializer_obj

        def get_queryset(self):
            """Query of all Participant objects being related to the given Event"""

            return model.objects.filter(event=self.kwargs["event_pk"])

        def get_event(self):
            """Gets queryset for Event objects with given pk"""

            query = Event.objects.filter(pk=self.kwargs["event_pk"])
            return get_object_or_404(query)

    return RelationshipViewset


def create_viewset(serializer, model):
    """
    Creates detailed viewsets for database objects
    :param serializer: serializer class
    :param model: database model
    :return: new viewset class
    """

    class Viewset(viewsets.ModelViewSet):
        """Viewset for non-nested objects"""

        def __init__(self, *args, **kwargs):
            self.__class__.__name__ = "{}".format(model.__name__)
            super().__init__(*args, **kwargs)

        serializer_class = serializer
        queryset = model.objects.all()

    return Viewset
