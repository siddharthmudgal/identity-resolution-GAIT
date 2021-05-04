from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(models.Model):
    """model to represent a user"""
    userid = models.CharField(max_length=255, unique=True)
    sensordata_x = ArrayField(models.CharField(max_length=255),
                              blank=False, default=list)
    sensordata_y = ArrayField(models.CharField(max_length=255),
                              blank=False, default=list)
    sensordata_z = ArrayField(models.CharField(max_length=255),
                              blank=False, default=list)

    def __str__(self):
        return self.userid
