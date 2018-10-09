"""tsp URL Configuration

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
from apps.blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^catalogueInit/(?P<action>(read)|(write))/(?P<category_id>\d*)/?(?P<id>\d*)/?$', views.catalogueInit),
    url(r'^catalogueSave/?$', views.catalogueSave),
    url(r'^catalogueList/(?P<category_id>\d*)/?(?P<page_number>\d)*/?$', views.catalogueList),
    url(r'^catalogueListData/(?P<page_limit>\d*)/?(?P<page_number>\d*)/?$', views.catalogueListData),
    url(r'^categoryAllList/?$', views.categoryAllList),
]

