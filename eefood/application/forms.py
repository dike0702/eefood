from django import forms
from django.forms import ModelForm
from .models import Restaurants, Reservation, Review
from django.core.validators import MaxLengthValidator

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

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), validators=[MaxLengthValidator(300)])
    class Meta:
        model = Review
        fields = ['title', 'comment', 'rate']

    def save(self, restaurant=None, author=None, commit=True):
        review = super().save(commit=False)
        review.restaurant = restaurant
        review.author = author
        if commit:
            review.save()
        return review
