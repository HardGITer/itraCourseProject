from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('cabinet/', views.cabinet),
    path('cabinet/createArticle/', views.createArticle),
]