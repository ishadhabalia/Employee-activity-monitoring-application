"""ets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ets.apis.views.user_data_view import GetData
from ets.apis.views.data_collection_view import CollectData

urlpatterns = [
    path('admin/', admin.site.urls),
    path('activity',GetData.as_view(), name='get-activity'),
    path('update-activity', CollectData.as_view(), name='update-activity'),
    path('', include('dashboard.urls')),
    path('', include('user.urls')),
]