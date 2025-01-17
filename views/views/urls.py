"""
URL configuration for views project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage_render),
    path('black_and_white/', black_and_white, name='black_and_white'),
    path('grey/', grey, name='grey'),
    path('resizing_first/', resizing_first, name='resizing_first'),
    path('resizing/', resizing, name='resizing'),
    path('align_vertical/', alignVertical, name='align_vertical'),
    path('align_horizontal/', alignHorizontal, name='align_horizontal'),
    path('fusionning/', fusionning, name='fusionning'),
    path('animation_first/',animation_first, name='animation_first'),
    path('animation/',animation, name='animation'),
]

