from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from organization.api.serializers import OrganizationSerializer
from organization.models import Organization


class OrganizationViewSet(mixins.UpdateModelMixin,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          mixins.RetrieveModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        status_filters = request.query_params.get('status', None).split(sep=',')
        queryset = self.get_queryset()
        if status_filters is not None:
            queryset = queryset.filter(status__in=status_filters)
        serializer = OrganizationSerializer(queryset, many=True)
        return Response(serializer.data)
