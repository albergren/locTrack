from django.contrib.gis.db import models

# Create your models here.

class TrackPoint(models.Model):
    timestamp = models.DateTimeField()
    point = models.PointField(geography=True)
    elevation = models.FloatField()
    speed = models.FloatField(null=True)

"""
class File(models.Model):
    time_start = 
    time_end = 
    number_of_points =
    hash =
    path =

"""
