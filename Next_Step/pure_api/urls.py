"""Next_Step URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name="PURE_API"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^yo/(?P<id>\d+)/',views.CBV.as_view()),
    url(r'^get/', views.CBV.as_view()),
    url(r'^post/',views.CBV.as_view()),
    url(r'^del/(?P<id>\d+)', views.CBV.as_view()),
    url(r'^put/(?P<id>\d+)', views.CBV.as_view()),
]
