from rest_framework import mixins
from rest_framework import viewsets

from organization.api.serializers import OrganizationSerializer
from organization.models import Organization


class OrganizationViewSet(mixins.UpdateModelMixin,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
