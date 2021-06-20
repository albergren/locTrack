from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.conf import settings
from django.core import serializers
from .models import TrackPoint
from django.contrib.gis.geos import Point

import gpxpy
import os

from django.template import loader

def index(request):

    template = loader.get_template('mapVisual/index.html')

    return HttpResponse(template.render(context, request))


def get_file(request, file_name):

    path = os.path.join(settings.BASE_DIR, 'mapVisual')
    response = FileResponse(open(path + '/static/mapVisual/' + file_name + '.geojson', 'rb'))

    return response

def import_data_gpx(request):

    for key in request.FILES:

        print(request.FILES[key])
        file_name = request.FILES[key]
        gpx = gpxpy.parse(file_name)

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    
                    print('Point at ({0},{1}) -> {2} at time {3}'
                          .format(point.latitude, point.longitude, point.elevation, point.time))

                    p = TrackPoint(timestamp=point.time,
                                   point=Point(point.latitude, point.longitude),
                                   elevation=point.elevation,
                                   speed=point.speed)

                    p.save()

    return HttpResponse(status=200)
