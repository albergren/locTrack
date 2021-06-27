from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, JsonResponse
from django.conf import settings
from django.core.serializers import serialize
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

def get_track_points(request):

    start = request.GET.get('start', '')
    end = request.GET.get('end', '')

    trackpoints = TrackPoint.objects.filter(timestamp__range=[start,end])
    trackpoints_serialized = serialize('geojson', trackpoints, geometry_field='point',fields=('timestamp',))

    return JsonResponse(trackpoints_serialized, safe=False)

def import_data_gpx(request):

    for key in request.FILES:

        print(request.FILES[key])
        file_name = request.FILES[key]
        gpx = gpxpy.parse(file_name)

        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    
                    print('Point at ({0},{1}) -> {2} at time {3}'
                          .format(point.latitude, point.latitude, point.elevation, point.time))

                    p = TrackPoint(timestamp=point.time,
                                   point=Point(point.longitude, point.latitude),
                                   elevation=point.elevation,
                                   speed=point.speed)

                    p.save()

    return HttpResponse(status=200)
