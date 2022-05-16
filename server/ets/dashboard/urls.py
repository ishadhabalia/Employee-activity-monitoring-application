from django.urls import path
from . import views

urlpatterns = [
# path('dashboard/<str:empid>/', views.dashboard, name = 'DashBoard'),
path('', views.view_dashboard, name = 'ViewDashBoard'),
]