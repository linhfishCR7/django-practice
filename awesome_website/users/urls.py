# users/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path("dashboard", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("oauth/", include("social_django.urls")),

]