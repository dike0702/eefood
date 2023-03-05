# from django.contrib.auth.forms import AuthenticationForm

# class LoginForm(AuthenticationForm):
#     def init(self, *args, **kwargs):
#         super().init(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs["class"] = "form-control"

from django import forms


class ReviewForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title')
    comment = forms.CharField(label='Comment', widget=forms.Textarea())
    
