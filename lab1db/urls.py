"""lab1db URL Configuration

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
from lab1db import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', views.lab1db),
    url(r'^lab1db/', views.lab1db , name='lab1db'),
    url(r'^new_agency',views.createagency),
    url(r'^new_tour',views.createtour),
    url(r'^new_dependency',views.createdependency),
    url(r'^delete_agency',views.deleteagency),
    url(r'^delete_dependency',views.deletedependency),
    url(r'^delete_tour',views.deletetour),
    url(r'^find_agency',views.findagency),
    url(r'^find_tour',views.findtour),
]
