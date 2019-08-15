from rest_framework import mixins
from rest_framework import viewsets

from engagement.api.serializers import EngagementSerializer
from engagement.models import Engagement
from common.permissions.engagement_permissions import EngagementPermissions


class EngagementViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):

    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
    permission_classes = [EngagementPermissions]
