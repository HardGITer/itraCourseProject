from django.conf.urls import url
from django.urls import path
# from . import views
from CourseProject import views

urlpatterns=[
    path('', views.index, name="main_page"),
    path('cabinet/<int:userid>/', views.cabinet),
    path('cabinet/<int:userid>/create/', views.create, name="create_article"),
    path('cabinet/<int:userid>/edit/<int:id>/', views.edit),
    path('adminEdit/<int:id>/', views.adminEdit),
    path('cabinet/<int:userid>/delete/<int:id>/', views.delete, name="delete_article"),
    path('view/<int:id>/', views.view),
    path('cabinet/output', views.output),
    path('testSearch', views.absoluteSearch, name="test_search"),
    path('editUser', views.editUser, name="edit_user"),
    path('changeTheme', views.changeTheme, name='change_theme'),
]