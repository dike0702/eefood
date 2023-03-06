from django import forms
from django.forms import ModelForm
from .models import Restaurants

class PostRestaurantForm(ModelForm):
    class Meta:
        model = Restaurants
        fields = "__all__"

class ReviewForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title')
    comment = forms.CharField(label='Comment', widget=forms.Textarea())
    
