from django.db import models
from django.core import validators


class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(100)
        ]
    )