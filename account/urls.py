"""django1234 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views

from account import views

app_name = "account"

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name="user_logout"),
    path('login/', auth_views.LoginView.as_view(template_name="account/login.html"), name="user_login"),
    path('register/', views.register, name='user_register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name="account/password_change_form.html", success_url="/account/password-change-done/"), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name="account/password_change_done.html"), name='password_change_done'),
]
