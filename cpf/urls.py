from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^app/consultacpf/$', views.cpf_app, name='cpf_app'),

]
