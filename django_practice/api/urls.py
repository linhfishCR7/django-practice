"""django_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from muilti_lang import views
from account.views import demo_recaptcha
from whatever.api import WhateverResource
whatever_resource = WhateverResource()
# urlpatterns = i18n_patterns(
#     path('admin/', admin.site.urls),
#     # path('api/', include('muilti_lang.urls'), name='muilti_lang'),
#     path('about/', views.about, name='about'),

# )
urlpatterns = [
   path('api/auth/', include('account.urls'), name='auth'),
   path('demo-recaptcha/', demo_recaptcha, name="demo"),
   path('api/', include(whatever_resource.urls)),
   path('api/', include('puppies.urls')),
]