from django.db import models

from common.enums import ProgressStatus
from common.models import BaseModel
from employee.models import Employee
from organization.models import Organization
from task.models import Task


class TaskAssignment(BaseModel):
    """Model that holds information about task assignments."""

    class Meta:
        db_table = 'task_assignment'

    status = models.CharField(
        max_length=100,
        choices=[(status.value, status.value) for status in ProgressStatus])
    start_date_time = models.DateTimeField(null=True, blank=True)
    end_date_time = models.DateTimeField(null=True, blank=True)
    task = models.ForeignKey(Task,
                             null=True,
                             on_delete=models.SET_NULL)
    employee = models.ForeignKey(Employee,
                                 null=True,
                                 on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)

    def __str__(self):
        return '%s - %s' % (str(self.task), str(self.employee))
