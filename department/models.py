"""Department app model"""
from common.models import BaseModel
from django.db import models
from organization.models import Organization


class Department(BaseModel):
    """
    Department model class.

    Holds department information.
    """
    name = models.CharField(max_length=128)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return self.name
