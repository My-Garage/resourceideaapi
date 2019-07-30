from django.db import models
from common.models import BaseModel
from engagement.models import Engagement
from organization.models import Organization
from common.enums import ProgressStatus
from employee.models import Employee


class Job(BaseModel):
    """Model to hold information about jobs."""

    class Meta:
        db_table = 'job'

    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    planned_start_date = models.DateField(null=True, blank=True)
    actual_start_date = models.DateField(null=True, blank=True)
    planned_end_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[(status.value, status.value) for status in ProgressStatus])
    engagement = models.ForeignKey(Engagement,
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   blank=True)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL,
                                     blank=True)
    manager = models.ForeignKey(Employee,
                                null=True,
                                on_delete=models.SET_NULL,
                                blank=True,
                                related_name='manager_jobs')

    def __str__(self):
        return self.title
