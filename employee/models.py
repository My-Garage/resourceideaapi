from django.contrib.auth.models import User
from django.db import models

from common.enums import Status
from common.models import BaseModel
from job_position.models import JobPosition
from organization.models import Organization


class Employee(BaseModel):
    """Employee model."""

    file_number = models.CharField(max_length=10, unique=True, null=True,
                                   blank=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True)
    phone_number_confirmed = models.BooleanField(null=False, default=False)
    status = models.CharField(
        max_length=10,
        choices=[(status.value, status.value) for status in Status])

    user = models.OneToOneField(User,
                                null=True,
                                on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)
    is_resource = models.BooleanField(null=False, default=False)
    email_confirmed = models.BooleanField(null=False, default=False)
    job_position = models.ForeignKey(JobPosition,
                                     null=True,
                                     on_delete=models.SET_NULL)
    date_terminated = models.DateField(null=True, blank=True)
    src_resource_id = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        db_table = 'employee'

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
