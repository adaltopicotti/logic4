from django.db import models
from django.core.validators import MinValueValidator
from .fields import *

# Create your models here.
class Coordinate(models.Model):
    lat_deg = models.IntegerField()
    lat_min = models.IntegerField()
    lat_sec = models.FloatField()
    lon_deg = models.IntegerField()
    lon_min = models.IntegerField()
    lon_sec = models.FloatField()
