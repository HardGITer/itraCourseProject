from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    url('login/', views.LoginFormView.as_view(), name="login"),
    url('register/', views.RegisterFormView.as_view(), name="register"),
    path('logout/', views.logoutView, name="logout"),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
