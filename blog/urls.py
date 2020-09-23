from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import include

app_name='blog'

urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    path('poast/<int:pk>/', views.PostDV.as_view(), name='post_detail'),
    path('archive/<int:year>/',views.PostYAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<str:month>/',views.PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/',views.PostDAV.as_view(), name='post_day_archive'),
    path('archive/today/',views.PostTAV.as_view(), name='post_today'),
]
