from django.shortcuts import render,redirect
from django.views import View
from django.http.response import HttpResponseRedirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin   # ログインを強制させる
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/profile.html')

class Login(LoginView):
    template_name = 'registration/login.html'
    form_class = LoginForm

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
