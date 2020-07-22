from rest_framework import mixins
from rest_framework import viewsets

from client.api.serializers import ClientSerializer
from client.models import Client
from common.utils.queryset import filter_organization_active_clients


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Client view set"""

    queryset = Client.objects.none()
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = filter_organization_active_clients(model=Client,
                                                      organization_id=self.request.user.employee.organization_id)
        return queryset

