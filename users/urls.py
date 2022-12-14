from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.userdashbord,name='userdashbord'),
    path('userposts', views.userposts,name='userposts'),
    path('user_profile/<str:pk>/', views.user_profile,name='user_profile'),   
]
