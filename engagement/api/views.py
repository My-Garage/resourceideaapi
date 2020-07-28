from rest_framework import mixins
from rest_framework import viewsets

from common.utils.queryset import filter_by_organization
from engagement.api.serializers import EngagementSerializer
from engagement.models import Engagement


class EngagementViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    queryset = Engagement.objects.none()
    serializer_class = EngagementSerializer

    def get_queryset(self):
        queryset = filter_by_organization(model=Engagement, organization_id=self.request.user.employee.organization_id)
        return queryset
