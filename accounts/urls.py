from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    DashboardAPIView
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    path('register/', RegisterAPIView.as_view()),

    path('login/', LoginAPIView.as_view()),

    path('token/refresh/', TokenRefreshView.as_view()),

    path('dashboard/', DashboardAPIView.as_view()),
]