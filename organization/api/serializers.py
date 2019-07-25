from organization.models import Organization
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    """Organization serializer"""

    class Meta:
        model = Organization
        exclude = ('created_at', 'updated_at', )
