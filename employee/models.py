from django.db import models
from common.models import BaseModel
from common.enums import Status
from organization.models import Organization
from django.contrib.auth.models import User


class Employee(BaseModel):
    """Employee model."""

    file_number = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    phone_number_confirmed = models.BooleanField(null=False, default=False)
    status = models.CharField(
        max_length=10,
        choices=[(Status.value, Status.value) for status in Status])

    user = models.OneToOneField(User,
                                null=True,
                                on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
