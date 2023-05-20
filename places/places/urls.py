from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    re_path(r'^places/', views.PlaceList),
    re_path(r'^placescreate/$', csrf_exempt(views.PlaceCreate), name='placesCreate'),
    re_path(r'^createplaces/$', csrf_exempt(views.PlaceCreate), name='createPlaces'),
]