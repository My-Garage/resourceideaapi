import re

from django.db import models

from common.models import BaseModel
from organization.models import Organization


class ClientIndustry(BaseModel):
    """Client industry model"""

    name = models.CharField(max_length=100, unique=True, null=False)
    name_slug = models.CharField(max_length=100,
                                 editable=False,
                                 null=False,
                                 unique=True)
    organization = models.ForeignKey(Organization,
                                     null=True,
                                     on_delete=models.SET_NULL)

    class Meta:
        db_table = 'client_industry'
        verbose_name_plural = 'Client Industries'
        unique_together = ['name', 'name_slug', 'organization']

    def save(self, *args, **kwargs):
        self.name_slug = re.sub(r'\W', '-', self.name.lower())
        super(ClientIndustry, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
