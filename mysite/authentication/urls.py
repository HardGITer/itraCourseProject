from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    url('login/', views.LoginFormView.as_view()),
    url('register/', views.RegisterFormView.as_view()),
]