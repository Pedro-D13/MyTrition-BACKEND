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
from allauth.account.views import confirm_email

urlpatterns = [
    path('foodsearch/', include('foodsearch.urls')),
    path("rest-auth/", include('rest_auth.urls')), 
    path("rest-auth/registration/", include("rest_auth.registration.urls")),
    path('users/', include('django.contrib.auth.urls')),
    # path('profile/', )
    path('admin/', admin.site.urls),
    # path('account-confirm-email/<r"^(?P<slug>[-\w]+)/$">', confirm_email, name="account_confirm_email"),
]

 
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns




