from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.conf import settings
import os

from django.template import loader

def index(request):
    template = loader.get_template('mapVisual/index.html')
    return HttpResponse(template.render(context, request))


def get_file(request, file_name):
    path = os.path.join(settings.BASE_DIR, 'mapVisual')
    response = FileResponse(open(path + '/static/mapVisual/' + file_name + '.geojson', 'rb'))
    return response

def upload_files(request):
    None
