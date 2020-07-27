"""MyTritionProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path , include
from django.conf import settings
from django.contrib.auth import views as auth_views

from django.urls import re_path
from django.conf.urls import url

from accounts.views import AccountsFavFoodListVS
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('foodsearch/', include('foodsearch.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('users/', include('django.contrib.auth.urls')),
    path('profile/', AccountsFavFoodListVS.as_view({'get':'list'})),
    path('profile/<int:fdc_id_arg>/', AccountsFavFoodListVS.as_view({'post':'create','delete':'destroy'})),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns





