from django.urls import path
from .views import CustomUserList, RegisterView, CustomAuthToken

urlpatterns = [
    path('users/', CustomUserList.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]