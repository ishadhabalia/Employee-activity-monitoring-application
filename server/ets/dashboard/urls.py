from django.urls import path
from . import views

urlpatterns = [
# path('dashboard/<str:empid>/', views.dashboard, name = 'DashBoard'),
path('dashboard/<int:user_id>/', views.view_dashboard, name = 'ViewDashBoard'),
path('teams/<int:user_id>/', views.view_teams, name = 'Teams'),
path('teams/<int:user_id>/<str:teamname>/', views.view_team_details, name = 'TeamDetails'),
]