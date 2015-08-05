from django.conf.urls import include, url
from django.contrib import admin
from Home import views

urlpatterns = [
    url(r'^$', views.HomeMain, name='Home'),
    url(r'^About/', views.About, name='About'),
]
