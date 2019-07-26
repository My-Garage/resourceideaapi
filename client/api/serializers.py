from rest_framework import serializers
from organization.api.serializers import OrganizationSerializer
from client_industry.api.serializers import ClientIndustrySerializer
from client.models import Client


class ClientSerializer(serializers.ModelSerializer):
    """Client serializer"""

    client_industry_id = serializers.UUIDField(write_only=True)
    client_industry = ClientIndustrySerializer(read_only=True)
    organization_id = serializers.UUIDField(write_only=True)
    organization = OrganizationSerializer(read_only=True)
    name_slug = serializers.CharField(read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'name_slug', 'address', 'organization',
                  'organization_id', 'client_industry', 'client_industry_id', )
