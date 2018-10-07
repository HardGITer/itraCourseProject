from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('likePost/', views.like_post, name="like_post"),
    path('comment/', views.add_comment, name="add_comment"),
    path('checkComment', views.check_comment, name="check_comment"),
    path('addRating/', views.add_rating, name="add_rating"),
    path('tag/', views.get_tags, name="get_tag"),
]