from django.conf.urls import include, url
from django.contrib import admin
from Hunt import views

urlpatterns = [
    url(r"^HuntMain/$", views.Main, name="HuntMain"),
    url(r"HuntBegin/(?P<HuntPk>[0-9]+)/$", views.HuntBegin, name="HuntBegin"),
    url(r"HuntDetail/([0-9]+)/([0-9]+)/$", views.HuntDetail, name="HuntDetail"),
]
