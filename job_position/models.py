from django.db import models
from common.models import BaseModel
from department.models import Department
from organization.models import Organization


class JobPosition(BaseModel):
    """
    Job positions class model.

    Holds information about the job positions.
    """

    title = models.CharField(max_length=128)
    hierarchy_order = models.IntegerField()
    department = models.ForeignKey(Department,
                                   null=True,
                                   on_delete=models.SET_NULL)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)
    src_job_position_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'job_position'

    def __str__(self):
        return self.title
