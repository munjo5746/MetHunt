from django.conf.urls import include, url
from django.contrib import admin
from Home import views

urlpatterns = [
    url(r'^$', views.home, name='Home'),
]
