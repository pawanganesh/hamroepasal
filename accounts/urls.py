from django.urls import path

from .views import (RegisterGenericAPIView, LoginGenericAPIView)

urlpatterns = [
    path('auth/register/', RegisterGenericAPIView.as_view()),
    path('auth/login/', LoginGenericAPIView.as_view()),
]
