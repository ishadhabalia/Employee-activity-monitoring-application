from django.urls import path
from . import views

urlpatterns = [
path('login', views.login, name = 'Login'),
path('profile', views.dispProfile, name = 'Profile'), #'profile/<str:empid>/'
]