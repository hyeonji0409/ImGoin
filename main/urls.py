from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    path('location/', views.location, name='location'), 
    path('write/', views.write, name='write'),
    path('account/', views.account, name='account'),
]
