from django.conf.urls import include, url
from django.contrib import admin
from UserAuthentication import views

urlpatterns = [
    url(r'^SignUp/$', views.SignUp, name='SignUp'),
    url(r'^LogIn/$', views.LogIn, name='LogIn'),
    url(r'^Profile/$', views.Profile, name='Profile'),
    url(r'^Logout/$', views.Logout, name="Logout"),
]
