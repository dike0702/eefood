from django.shortcuts import render
from django.views.generic import View
from .models import Restaurants
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin

# from . import forms

class IndexView(View):
    def get(self, request, *args, **kwargs):
        restaurant_data = Restaurants.objects.all()
        return render(request, 'application/index.html', {
            'restaurant_data': restaurant_data
        })

class ItemDetailView(View):
    def get(self, request, *args, **kwargs):
        restaurant_data = Restaurants.objects.get(name=self.kwargs['name'])
        return render(request, 'application/restaurant.html', {
            'restaurant_data': restaurant_data
        })

# class Review(TemplateView):
#     template_name = "review.html"

# # class HomeView(LoginRequiredMixin, TemplateView):
# class HomeView(TemplateView):
#     template_name = "home.html"
#     # login_url = "/login"

# class LoginView(LoginView):
#     form_class = forms.LoginForm
#     template_name = "login.html"

# class LogoutView(LoginRequiredMixin, LogoutView):
#     template_name = "login.html"
