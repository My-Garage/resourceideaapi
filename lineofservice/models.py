from django.db import models

from common.models import BaseModel
from organization.models import Organization


class LineOfService(BaseModel):
    """Line of service model"""

    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)

    class Meta:
        db_table = 'line_of_service'
        verbose_name_plural = 'Lines of Service'
