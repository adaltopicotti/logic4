from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^app/geotools/coordinate/$', views.coordinate, name='coordinate'),

]
