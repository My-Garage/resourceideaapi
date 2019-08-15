from rest_framework import serializers
from rest_framework.reverse import reverse

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee serializer"""

    organization_id = serializers.UUIDField()
    user_id = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = ('id', 'file_number', 'phone_number',
                  'phone_number_confirmed', 'status',
                  'organization_id', 'user_id', 'is_resource', )


class ManagerSerializer(serializers.ModelSerializer):
    """Manager serializer"""

    fullname = serializers.SerializerMethodField(
        read_only=True,
        method_name='get_user_fullname')
    link = serializers.SerializerMethodField(
        read_only=True,
        method_name='get_manager_link')

    def get_user_fullname(self, obj):
        return f'{obj.user.get_full_name()}'

    def get_manager_link(self, obj):
        return reverse('employee-detail',
                       args=[obj.id],
                       request=self.context['request'])

    class Meta:
        model = Employee
        fields = ['fullname', 'link']
