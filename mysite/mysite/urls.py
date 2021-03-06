"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('main/', include('CourseProject.urls'), name="home_page"),
    path('authentication/', include('authentication.urls')),
    path('accounts/', include('allauth.urls')),
    path('feedback/', include('Feedback.urls')),
    path('search/', include('Search.urls')),
    url(r'^messages/', include('postman.urls', namespace='postman')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
#
# urlpatterns += i18n_patterns(
#     path('admin/', admin.site.urls),
#     path('main/', include('CourseProject.urls')),
#     path('authentication/', include('authentication.urls')),
#     path('accounts/', include('allauth.urls')),
#     prefix_default_language=True,
# )
