# from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^details/(?P<id>\d+)/$', views.details, name='details')
]