from django.contrib import admin
from django.urls import path, include
import main.views
import blog.views
#import login.views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name='home'),
    path('main/', include('main.urls')),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),
]
