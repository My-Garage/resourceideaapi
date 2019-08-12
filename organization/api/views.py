from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from organization.api.serializers import OrganizationSerializer
from organization.models import Organization


class OrganizationViewSet(mixins.UpdateModelMixin,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated, )
