
from django.urls import path
from .views import RegisterUserAPIView, GetListUserAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name='auth_register'),
    path('list-users/', GetListUserAPIView.as_view(), name='list-users'),
]