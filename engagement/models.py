from django.db import models
from common.models import BaseModel
from organization.models import Organization
from employee.models import Employee
from client.models import Client
from lineofservice.models import LineOfService
from common.enums import ProgressStatus


class Engagement(BaseModel):
    """Model holds information about the engagement details."""

    class Meta:
        db_table = 'engagement'

    title = models.CharField(max_length=256)
    description = models.TextField()
    planned_start_date = models.DateField()
    actual_start_date = models.DateField(null=True, blank=True)
    planned_end_date = models.DateField()
    actual_end_date = models.DateField(null=True, blank=True)
    color = models.CharField(max_length=7)
    status = models.CharField(
        max_length=10,
        choices=[(status.value, status.value) for status in ProgressStatus])
    manager = models.ForeignKey(Employee,
                                null=True,
                                on_delete=models.SET_NULL)
    partner = models.ForeignKey(Employee,
                                null=True,
                                on_delete=models.SET_NULL)
    client = models.ForeignKey(Client,
                               null=True,
                               on_delete=models.SET_NULL)
    line_of_service = models.ForeignKey(LineOfService,
                                        null=True,
                                        on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
