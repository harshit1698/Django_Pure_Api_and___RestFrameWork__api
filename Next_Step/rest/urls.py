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
from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name="Rest"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^pure/',include("pure_api.urls")),
    url(r'^list/',views.Create.as_view()),
    url(r'^gett/(?P<id>\d+)',views.details.as_view()),
    url(r'^c1/',views.CBV_create.as_view()),
    url(r'^del/(?P<id>\d+)',views.Del.as_view()),
    url(r'^up/(?P<id>\d+)',views.Up.as_view()),
    url(r'^all/',views.APIVieww.as_view()),
    url(r'^begin',views.Beginning.as_view()),
    url(r'^show/',views.List.as_view()),
    url(r'^yo/(?P<id>\d+)',views.Ree.as_view()),
    url(r'^see/',views.YoBoy.as_view(),name="Ap"),
    url(r'^register/',views.RegisterView.as_view())

]

