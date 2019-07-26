from rest_framework import mixins
from rest_framework import viewsets
from client.api.serializers import ClientSerializer
from client.models import Client


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """Client view set"""

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
