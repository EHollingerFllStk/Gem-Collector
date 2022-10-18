from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Gem(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    uses = models.CharField(max_length=100)

    def __str__(self):
        return self.name