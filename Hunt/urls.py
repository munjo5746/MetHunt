from django.conf.urls import include, url
from django.contrib import admin
from Hunt import views

urlpatterns = [
    url(r"^HuntMain/$", views.Main, name="HuntMain"),
    url(r"HuntBegin/(?P<HuntPk>\d+)/$", views.HuntBegin, name="HuntBegin"),
]
