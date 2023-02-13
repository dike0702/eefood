from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from . import forms



class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "daiki"
        return ctxt

class Review(TemplateView):
    template_name = "review.html"

# class HomeView(LoginRequiredMixin, TemplateView):
class HomeView(TemplateView):
    template_name = "home.html"
    # login_url = "/login"

class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "login.html"
