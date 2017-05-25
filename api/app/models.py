from __future__ import unicode_literals
from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    college = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s %s %s %s' % (self.id, self.first_name, self.last_name, self.college)

# Create your models here.
