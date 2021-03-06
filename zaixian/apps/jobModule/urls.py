"""zaixian URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from apps.jobModule.views import *

app_name = 'jobModule'
urlpatterns = [
    url(r'^edit/(?P<jobInfo_id>\d+)(/(?P<id>\d+))?/?$', edit),
    url(r'^save/?$', save),
    url(r'^lol/?$',lol),
    url(r'^show/$',list,),
    url(r'^show/$',yaya),
    url(r'^table/(?P<action>(read)|(write))/(?P<id>\d*)/?$', table),
    url(r'^list/(?P<page_limit>\d*)/?$', list),
    url(r'^listData/(?P<page_limit>\d*)/?(?P<page_number>\d*)/?$', listData),
    url(r'^delete/$', delete),
]
