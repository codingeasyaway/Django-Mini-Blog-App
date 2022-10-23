"""miniblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='Home Page'),
    path('About/', views.About, name='About Us'),
    path('Contact/', views.Contact, name='Contact Us'),
    path('Dashboard/', views.Dashboard, name='Dashboard'),
    path('AddPost/', views.AddPost, name='Add Post'),
    path('UpdatePost/<int:id>/', views.UpdatePost, name='Update Post'),
    path('DeletePost/<int:id>/', views.DeletePost, name='Delete Post'),
    path('User_Signup/', views.User_Signup, name='Signup Page'),
    path('User_Login/', views.User_Login, name='Login Page'),
    path('User_Logout/', views.User_Logout, name='Logout'),


]
