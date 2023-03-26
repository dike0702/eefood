from django import forms
from django.forms import ModelForm
from .models import Restaurants, Reservation

class PostRestaurantForm(ModelForm):
    class Meta:
        model = Restaurants
        fields = "__all__"

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'num_people']
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
            'time': forms.TextInput(attrs={'type': 'time'})
        }

class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, required=False, label='')

class ReviewForm(forms.Form):
    title = forms.CharField(max_length=255, label='Title')
    comment = forms.CharField(label='Comment', widget=forms.Textarea())
    
