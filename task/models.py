from django.db import models

from common.enums import ProgressStatus
from common.models import BaseModel
from job.models import Job
from organization.models import Organization


class Task(BaseModel):
    """Model that holds information about tasks."""

    class Meta:
        db_table = 'task'

    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    status = models.TextField(
        max_length=20,
        default=ProgressStatus.NOT_STARTED.value,
        choices=[(status.value, status.value) for status in ProgressStatus])
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL,
                                     blank=True)
    job = models.ForeignKey(Job,
                            null=True,
                            on_delete=models.SET_NULL,
                            blank=True)
    src_job_id = models.CharField(max_length=40, null=True, blank=True)
    start_date_time = models.DateTimeField(null=True, blank=True)
    end_date_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
