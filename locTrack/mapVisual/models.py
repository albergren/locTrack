from django.contrib.gis.db import models

# Create your models here.

class TrackPoint(models.Model):
    timestamp = models.DateTimeField()
    point = models.PointField(geography=True)
    elevation = models.FloatField()
    speed = models.FloatField(null=True)


class Location(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    time_until_visited = models.IntegerField()
    color = models.CharField(max_length=7)
    polygon = models.PolygonField()
    

    
