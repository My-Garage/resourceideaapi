from rest_framework import mixins
from rest_framework import viewsets

from client.api.serializers import ClientSerializer
from client.models import Client
from client.permissions import ClientPermissions


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    """Client view set"""

    queryset = Client.objects.none()
    serializer_class = ClientSerializer
    permission_classes = [ClientPermissions]

    def get_queryset(self):
        return Client.objects.filter(
            organization_id=self.request.user.employee.organization_id)\
            .all()
