from django.contrib.postgres.fields import ArrayField
from django.db import models


class User(models.Model):
    """model to represent a user"""
    userid = models.CharField(max_length=255)
    sensordata_x = ArrayField(models.DecimalField(decimal_places=5,
                                                  max_digits=10),
                              blank=False, default=list)
    sensordata_y = ArrayField(models.DecimalField(decimal_places=5,
                                                  max_digits=10),
                              blank=False, default=list)
    sensordata_z = ArrayField(models.DecimalField(decimal_places=5,
                                                  max_digits=10),
                              blank=False, default=list)

    def __str__(self):
        return self.userid
