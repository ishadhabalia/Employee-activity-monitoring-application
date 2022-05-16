from django.shortcuts import render

# Create your views here.

def view_dashboard(request):
     return render(request,'dashboard/dashboard_home.html',{'nbar': 'home','role':'manager'})

def view_teams(request):
     return render(request,'dashboard/teams.html',{'nbar': 'teams','role':'manager'})