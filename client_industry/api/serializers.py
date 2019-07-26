from rest_framework import serializers

from client_industry.models import ClientIndustry
from organization.api.serializers import OrganizationSerializer


class ClientIndustrySerializer(serializers.ModelSerializer):
    """Client industry serializer"""

    organization_id = serializers.UUIDField(write_only=True)
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = ClientIndustry
        fields = ('id', 'name', 'name_slug', 'organization', 'organization_id')
