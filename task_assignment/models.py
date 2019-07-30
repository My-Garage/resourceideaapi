from django.db import models
from common.models import BaseModel
from task.models import Task
from employee.models import Employee


class TaskAssignment(BaseModel):
    """Model that holds information about task assignments."""

    class Meta:
        db_table = 'task_assignment'

    start_date_time = models.DateTimeField()
    completion_date_time = models.DateTimeField(null=True, blank=True)
    task = models.ForeignKey(Task,
                             null=True,
                             on_delete=models.SET_NULL)
    employee = models.ForeignKey(Employee,
                                 null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return '%s - %s' % (str(self.task), str(self.employee))
