from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-new-location/', views.add_new_location),
    path('get-all-locations/', views.get_all_locations),
    path('all-categories/', views.all_categories),
    path('child-categories/', views.child_categories),
    path('new-category/', views.new_category),
    path('remove-category/', views.remove_category),
    path('import-data-gpx/',views.import_data_gpx ),
    path('trackpoints/', views.trackpoints),
    path('<str:file_name>/', views.get_file),
]
