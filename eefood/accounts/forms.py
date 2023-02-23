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