from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    url('test', views.index),
    path('home', views.index),
    path('about', views.index)
]