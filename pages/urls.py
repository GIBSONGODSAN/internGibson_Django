# pages/urls.py

from django.urls import path
from pages import views
from pages.views import UserView
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('users/', views.UserView.as_view(), name='user-view'),
    path('api-token-auth/', obtain_jwt_token, name='api_token_auth'),
    path('api-token-refresh/', refresh_jwt_token, name='api_token_refresh'),
    path('api-token-verify/', verify_jwt_token, name='api_token_verify'),
]
