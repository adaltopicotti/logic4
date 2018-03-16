from django.conf.urls import url
from . import views as core_views
from django.contrib.auth import views



urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^accounts/signup/$', core_views.signup, name='signup'),
    url(r'^accounts/login/$', views.login, name='login'),
]
