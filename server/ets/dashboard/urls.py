from django.urls import path
from . import views

urlpatterns = [
# path('dashboard/<str:empid>/', views.dashboard, name = 'DashBoard'),
path('dashboard/', views.view_dashboard, name = 'ViewDashBoard'),
path('teams/', views.view_teams, name = 'Teams'),
path('teams/<str:teamname>/', views.view_team_details, name = 'TeamDetails'),
]