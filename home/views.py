from . import forms
from django.shortcuts import render
from . import models
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, TemplateView, ListView, DetailView


class IndexView(TemplateView):
    template_name = 'home/index.html'


class RegisterView(TemplateView):
    template_name = 'home/register.html'


class LoginView(TemplateView):
    template_name = 'home/login.html'


class LogoutView(TemplateView):
    template_name = 'home/logout.html'


class ProfileView(TemplateView):
    template_name = 'home/profile.html'


# @login_required
# class UserProfileDetailView(DetailView):
#     model = UserProfileInfo

