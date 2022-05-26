from django.shortcuts import render, redirect
from django.urls import reverse
from dashboard.services.get_user_data import get_user_buffer, get_user_location

# Create your views here.


def redirect_login(request):
    return redirect("Login")


def login(request):
    if request.method == "POST":
        if request.POST.get("password") == "manager":
            return redirect(reverse("ViewDashBoard", args=(1,)))
        return redirect(reverse("ViewDashBoard", args=(2,)))
    return render(request, "user/login.html", {"nbar": "login", "role": "employee"})


def dispProfile(request, user_id):
    user_data = get_user_buffer(user_id)
    user_location = get_user_location(user_id)
    user = {
        "name": user_data.name,
        "role": user_data.role,
        "joined_on": user_data.joined_on,
        "office_branch": "branch-abc",
        "city": user_location,
        "email": user_data.name + "@gmail.com",
    }
    team = {
        "dept": "Software Engineering",
        "team_name": "abcd",
        "no_members": 2,
        "manager": "manan",
        "team_members": [
            {"m_name": "saket", "m_role": "employee"},
            {"m_name": "isha", "m_role": "employee"},
        ],
    }
    context = {
        "user": user,
        "team": team,
        "nbar": "home",
        "role": user_data.role,
        "user_id": user_id,
    }
    return render(request, "user/profile.html", context)
