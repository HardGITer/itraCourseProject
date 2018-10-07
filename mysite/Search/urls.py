from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns=[
    path('tagSearch/<int:id>/', views.tagSearch, name="tag_search"),
]