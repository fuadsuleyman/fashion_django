from django.urls import path
from . import views
from .views import (
    register,
    auth_login,
)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.auth_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
