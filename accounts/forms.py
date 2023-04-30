from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ["email"]
    
    def __init__(self, email=None, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        if email:
            self.fields['email'].widget.attrs['value'] = email
    
    def update(self, user):
        user.email      = self.cleaned_data['email']
        user.save()