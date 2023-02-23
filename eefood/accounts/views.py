from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')

class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

class Logout(LogoutView):
    template_name = 'registration/logout.html'
