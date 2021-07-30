from django.shortcuts import render
from django.http import FileResponse, JsonResponse, HttpResponse
from django.conf import settings
from django.core.serializers import serialize
from .models import TrackPoint, Location
from django.contrib.gis.geos import Point, Polygon
import json

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

def add_new_location(request):
    req_json = json.loads(request.body)

    coords = json.loads(request.body)['polygon']['geometry']['coordinates'][0]
    coords.append(coords[0])
    coords_tuple = tuple(json.loads(request.body)['polygon']['geometry']['coordinates'][0])
    l = Location(name=req_json['name'],
                 category=req_json['category'],
                 time_until_visited=int(req_json['timeUntilVisited']),
                 color=req_json['color'],
                 polygon=Polygon(coords))

    l.save()
                                             
    return HttpResponse(status=200)

def get_all_locations(request):
    locations = Location.objects.all()
    locations_serialized = serialize('geojson', locations ,geometry_field='polygon',fields=('pk','name','color'))
    return JsonResponse(locations_serialized, safe=False)



