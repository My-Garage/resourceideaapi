import re

from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied

from client_industry.models import ClientIndustry
from organization.api.serializers import OrganizationSerializer


class ClientIndustrySerializer(serializers.ModelSerializer):
    """Client industry serializer"""

    organization_id = serializers.UUIDField(write_only=True)
    organization = OrganizationSerializer(read_only=True)

    class Meta:
        model = ClientIndustry
        fields = ('id', 'name', 'name_slug', 'organization', 'organization_id')

    def create(self, validated_data):
        organization_id = validated_data.get('organization_id', None)
        if organization_id is None:
            raise serializers.ValidationError('organization_id is required')

        user_organization_id = self.context['request'].user.employee.organization_id
        if organization_id != user_organization_id:
            raise PermissionDenied('User does not have the permission to perform action')

        client_industry_name = validated_data.get('name', None)
        if client_industry_name is None:
            raise serializers.ValidationError('name is required')

        return ClientIndustry.objects.create(name=client_industry_name, organization_id=organization_id)

    def update(self, instance, validated_data):
        name_slug = re.sub(r'\W', '-', validated_data['name'].lower())
        client_industry_with_slug: ClientIndustry = ClientIndustry.objects.filter(name_slug=name_slug).first()
        if client_industry_with_slug is not None and instance.id != client_industry_with_slug.id:
            raise serializers.ValidationError('Client industry with name already exists')

        instance.name = validated_data['name']
        instance.save()
        return instance
