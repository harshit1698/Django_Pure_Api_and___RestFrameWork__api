from django.conf.urls import url
from django.contrib import admin
from . import views

# app_name="PURE_API"

urlpatterns = [
   url(r'^$',views.Auth.as_view())
]