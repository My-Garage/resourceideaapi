from rest_framework import mixins
from rest_framework import viewsets

from engagement.api.serializers import EngagementSerializer
from engagement.models import Engagement
from engagement.permissions import EngagementPermissions


class EngagementViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    queryset = Engagement.objects.none()
    serializer_class = EngagementSerializer
    permission_classes = [EngagementPermissions]

    def get_queryset(self):
        return Engagement.objects.filter(
            organization_id=self.request.user.employee.organization_id)\
            .all()
