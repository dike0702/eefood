from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Restaurants, Review
from .forms import ReviewForm, PostRestaurantForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

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
        # form = PostRestaurantForm(request.POST or None)
        form = PostRestaurantForm(request.POST)
        
        if form.is_valid():
            # restaurant_data = Restaurants()
            # restaurant_data.name = form.cleaned_data['name']
            # restaurant_data.addr = form.cleaned_data['adr']
            # restaurant_data.table = form.cleaned_data['table']
            # restaurant_data.Genre = form.cleaned_data['Genre']
            # restaurant_data.phone = form.cleaned_data['phone']
            # restaurant_data.img = form.cleaned_data['img']
            # restaurant_data.save()
            form.save(commit=True)
            # return redirect('top')
        
        return render(request, 'application/index.html',{
            'form': form
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

