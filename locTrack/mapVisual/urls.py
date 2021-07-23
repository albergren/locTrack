from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-new-location/', views.add_new_location),
    path('get-all-locations/', views.get_all_locations),
    path('import-data-gpx/',views.import_data_gpx, name='import'),
    path('get-trackpoints/', views.get_track_points, name='trackpoints'),
    path('<str:file_name>/', views.get_file, name='get'),
]
