from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid

class departament(models.Model):
    ID = models.CharField(unique=True, null=True, blank=True, max_length=25)
    Organization = models.CharField(null=False, blank=False, max_length=155)
    name = models.CharField(null=False, blank=False, max_length=255)
    status = models.BooleanField(default=True, null=False)

    class Meta:
        ordering = ['id', 'Organization', 'status']


    def __str__(self):
        return " %s %s %s" % (self.ID, self.Organization, self.name, self.status)