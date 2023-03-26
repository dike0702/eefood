from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Restaurants, Review
from .forms import ReviewForm, PostRestaurantForm, ReservationForm, SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render

class IndexView(View):
    def get(self, request, *args, **kwargs):
        restaurant_data = Restaurants.objects.all()
        form = SearchForm(request.GET or None)
        return render(request, 'application/index.html', {
            'form': form,
            'restaurant_data': restaurant_data
        })
    
    def search(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = SearchForm(request.GET)
            restaurant_data = Restaurants.objects.all()
            if form.is_valid() and form.cleaned_data['search_query']:
                search_query = form.cleaned_data['search_query']
                restaurant_data = restaurant_data.filter(name__icontains=search_query)
            return render(request, 'application/search_result.html', {
                'form': form,
                'restaurant_data': restaurant_data
            })
        else:
            form = SearchForm()
            restaurant_data = Restaurants.objects.all()
        return render(request, 'reservation_create.html', {
            'form': form, 
            'restauant_data': restaurant_data
        })

class ItemDetailView(View):
    def get(self, request, *args, **kwargs):
        restaurant_data = Restaurants.objects.get(name=self.kwargs['name'])
        #review_data = Review.objects.all()
        review_data = Review.objects.order_by('-id')
        return render(request, 'application/restaurant.html', {
            'restaurant_data': restaurant_data,
            'review_data': review_data
        })

class PostRestaurantView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        form = PostRestaurantForm(request.POST or None)
        return render(request, 'application/postRestaurant.html',{
            'form': form
        })

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostRestaurantForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('top')
        else:
            form = PostRestaurantForm()
        return render(request, 'index.html',{
            'form': form
        })
    
class ReservationView(View):
    def get(self, request, *args, **kwargs):
        form = ReservationForm(request.POST or None)
        restaurant_data = Restaurants.objects.get(name=self.kwargs['name'])
        return render(request, 'application/reservation_create.html',{
            'form': form,
            'restaurant': restaurant_data
        })
        
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ReservationForm(request.POST or None)
            restaurant_data = Restaurants.objects.get(name=self.kwargs['name'])
            if form.is_valid():
                reservation = form.save(commit=False)
                reservation.restaurant = restaurant_data
                reservation.save()
                return redirect('top')
        else:
            form = PostRestaurantForm()
            restaurant_data = Restaurants.objects.get(name=self.kwargs['name'])
        return render(request, 'reservation_create.html', {
            'form': form, 
            'restaurant': restaurant_data
        })

class ReviewDetailView(View):
    def get(self, request, *args, **kwargs):
        review_data = Review.objects.get(id=self.kwargs['pk'])
        return render(request, 'application/review.html', {
            'review_data': review_data
        })
        
class CreateReviewView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = ReviewForm(request.POST or None)
        return render(request, 'application/review_form.html',{
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST or None)
        
        if form.is_valid():
            review_data = Review()
            review_data.author = request.user
            review_data.title = form.cleaned_data['title']
            review_data.comment = form.cleaned_data['comment']
            review_data.save()
            return redirect('review', review_data.id)
        
        return render(request, 'application/review_form.html',{
            'form': form
        })
        
class ReviewEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        review_data = Review.objects.get(id=self.kwargs['pk'])
        form = ReviewForm(
            request.POST or None,
            initial = {
                'title': review_data.title,
                'comment': review_data.comment
            }
        )
        
        return render(request, 'application/review_form.html',{
            'form': form
        })
        
    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST or None)
        
        if form.is_valid():
            review_data = Review.objects.get(id=self.kwargs['pk'])
            review_data.author = request.user
            review_data.title = form.cleaned_data['title']
            review_data.comment = form.cleaned_data['comment']
            review_data.save()
            return redirect('review', self.kwargs['pk'])
        
        return render(request, 'application/review_form.html',{
            'form': form
        })
        
class ReviewDeleteView(LoginRequiredMixin, View):
        def get(self, request, *args, **kwargs):
            review_data = Review.objects.get(id=self.kwargs['pk'])
            return render(request, 'application/review_delete.html', {
                'review_data': review_data
        })
            
        def post(self, request, *args, **kwargs):
            review_data = Review.objects.get(id=self.kwargs['pk'])
            review_data.delete()
            return redirect('top')

