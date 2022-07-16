"""backend URL Configuration

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
from django.urls import path
from userprofile.views import users,get_user_details,edit_user_profile,delete_user,search_users,sort_users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',users),
    path('api/user/<int:id>/',get_user_details),
    path('api/user_update/<int:id>/',edit_user_profile),
    path('api/user_delete/<int:id>/',delete_user),
    path('api/search_user/<str:name>/',search_users),
    path('api/sort_users/<str:name>/',sort_users)
]
