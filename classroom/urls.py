from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profesor/', views.profesorpage, name='profesorpage'),
    path('student/', views.studentpage, name='studentpage'),
    path('subject/', views.subjectpage, name='studentpage'),
    path('class/', views.classpage, name='classpage'),
]