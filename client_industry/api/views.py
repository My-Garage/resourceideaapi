from rest_framework import mixins
from rest_framework import viewsets

from client_industry.api.serializers import ClientIndustrySerializer
from client_industry.models import ClientIndustry


class ClientIndustryViewSet(mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """Client industry viewsets"""

    queryset = ClientIndustry.objects.all()
    serializer_class = ClientIndustrySerializer
