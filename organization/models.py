import re

from django.db import models

from common.enums import Status
from common.models import BaseModel


class Organization(BaseModel):
    """Organization model"""

    name = models.CharField(blank=False,
                            max_length=256,
                            null=False)
    name_slug = models.CharField(blank=True,
                                 null=False,
                                 max_length=256,
                                 unique=True,
                                 editable=False)
    status = models.CharField(
        max_length=10,
        choices=[(status.value, status.value) for status in Status])

    class Meta:
        db_table = 'organization'

    def save(self, *args, **kwargs):
        self.name_slug = re.sub(r'\W', '-', self.name.lower())
        super(Organization, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
