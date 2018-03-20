from django.conf.urls import url
from . import views as core_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^accounts/signup/$', core_views.signup, name='signup'),
    url(r'^accounts/login/$', core_views.login_site, name='login_site'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^accounts/auth/$', auth_views.login, name='login'),
]
