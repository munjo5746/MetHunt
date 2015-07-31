from django.conf.urls import include, url
from django.contrib import admin
from Hunt import views

urlpatterns = [
    url(r"^HuntMain/$", views.Main, name="HuntMain"),
    url(r"^HuntBegin/(?P<HuntPk>[0-9]+)/$", views.HuntBegin, name="HuntBegin"),
    url(r"^HuntDetail/(\d+)/(-?\d+)/$", views.HuntDetail, name="HuntDetail"),
    url(r"^HuntCorrect/(\d+)/(-?\d+)/$", views.HuntCorrect, name="HuntCorrect"),
    url(r"^HuntCongrat/$", views.HuntCongrat, name="HuntCongrat"),
]
