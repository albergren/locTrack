from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('import-data-gpx/',views.import_data_gpx, name='import'),
    path('get-trackpoints/', views.get_track_points, name='trackpoints'),
    path('<str:file_name>/', views.get_file, name='get'),
]
