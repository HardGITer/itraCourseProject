from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    url('login/', views.LoginFormView.as_view(), name="login"),
    url('register/', views.RegisterFormView.as_view(), name="register"),
    path('logout/', views.logoutView, name="logout"),
]