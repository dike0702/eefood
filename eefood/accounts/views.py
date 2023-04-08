from django.shortcuts import render,redirect
from django.views import View
from application.models import Reservation
from django.http.response import HttpResponseRedirect
from .forms import LoginForm, SignUpForm, UserChangeForm
from application.models import Reservation
from application.forms import ReservationForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin   # ログインを強制させる
from django.views.generic import CreateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user = self.request.user
        reservation = Reservation.objects.filter(name=user)
        return render(request, 'accounts/profile.html', {
            'reservation': reservation,
        })

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'application/reservation_delete.html'
    success_url = reverse_lazy('profile')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
    
class ReservationUpdateView(UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'application/reservation_update.html'
    success_url = reverse_lazy('profile')

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

class UserChangeView(LoginRequiredMixin, FormView):
    template_name = 'registration/change.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.update(user=self.request.user)
        return super().form_valid(form)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'email' : self.request.user.email,
        })
        return kwargs