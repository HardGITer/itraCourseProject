from django.conf.urls import url
from django.urls import path
# from . import views
from CourseProject import views

urlpatterns=[
    path('', views.index),
    path('cabinet/<int:userid>/', views.cabinet),
    path('cabinet/<int:userid>/create/', views.create),
    path('cabinet/<int:userid>/edit/<int:id>/', views.edit),
    path('cabinet/<int:userid>/delete/<int:id>/', views.delete),
    path('view/<int:id>/', views.view),
    path('cabinet/output', views.output),
    path('testSearch', views.absoluteSearch, name="test_search"),
]