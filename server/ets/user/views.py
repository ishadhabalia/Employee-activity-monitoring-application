from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'user/login.html',{'nbar': 'login','role':'manager'})

def dispProfile(request):
    return render(request,'user/profile.html',{'nbar': 'home','role':'manager'})
