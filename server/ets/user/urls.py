from django.urls import path
from . import views

urlpatterns = [
    path("", views.redirect_login, name="redirect"),
    path("login", views.login, name="Login"),
    path(
        "profile/<int:user_id>", views.dispProfile, name="Profile"
    ),  #'profile/<str:empid>/'
]
