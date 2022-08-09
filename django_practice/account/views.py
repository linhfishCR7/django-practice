from django.shortcuts import render
from rest_framework import generics
from .throttle import UserLoginRateThrottle
from .serializers import UserCreateSerializer, ListUserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import Throttled
from django.conf import settings
from django.shortcuts import render

# Create your views here.

class RegisterUserAPIView(generics.CreateAPIView):

    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer
    throttle_classes = (UserLoginRateThrottle,)

    def perform_create(self, serializer):
        user = serializer.save()

    def throttled(self, request, wait):
        raise Throttled(detail={
            "message": "recaptcha_required",
        })

class GetListUserAPIView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListUserSerializer
    throttle_classes = (UserLoginRateThrottle,)

    def get_queryset(self):
        return User.objects.all()

    def throttled(self, request, wait):
        raise Throttled(detail={
            "message": "recaptcha_required",
        })

def demo_recaptcha(request):
    return render(request, 'demo_recaptcha.html', {
        "key": settings.RE_CAPTCHA_SITE_KEY
    })