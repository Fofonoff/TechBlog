# from django.conf.urls import url
from django.urls import path

from . import views

# App urls
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('about/', views.about, name='blog-about'),
    path('details/', views.details, name='details')
]
