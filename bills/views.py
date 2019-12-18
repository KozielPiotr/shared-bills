# pylint: disable=too-many-ancestors,no-member, unused-argument
"""Views for bills application."""

from rest_framework import viewsets


def create_viewset(serializer, model, nested):
    """
    Creates viewsets for objects related to the Event object
    :param serializer:
    :param serializer: serializer class
    :param model: database model
    :param nested: if True, get_query function is overwritten, else queryset variable is set
    :return: new viewset class
    """

    class EventRelationshipsViewset(viewsets.ModelViewSet):
        """Viewsets for objects related to the Event object"""

        serializer_class = serializer
        if nested:

            def get_queryset(self):
                """Query of all Participant objects being related to the given Event"""

                return model.objects.filter(event=self.kwargs["event_pk"])

        else:
            queryset = model.objects.all()

    return EventRelationshipsViewset
