from django.urls import path
from accounts.views import RegisterAPI, LogoutAPI, CustomTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

urlpatterns = [
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterAPI.as_view(), name = "registerapi"),
    path('api/logout', LogoutAPI.as_view(), name= "logoutapi"),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    ]   