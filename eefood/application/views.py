from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Restaurants, Review
from django.contrib import messages
from .forms import ReviewForm, PostRestaurantForm, ReservationForm, SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic.edit import FormView

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
        form = PostRestaurantForm(request.POST)
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

class RestaurantReviewView(UserPassesTestMixin, View):
    def get(self, request, pk):
        restaurant = Restaurants.objects.get(name=pk)
        form = ReviewForm()
        context = {'restaurant': restaurant, 'form': form}
        return render(request, 'application/review_form.html', context)

    def post(self, request, pk):
        restaurant = Restaurants.objects.get(name=pk)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False, restaurant=restaurant, author=self.request.user)
            review.restaurant = restaurant
            review.author = request.user
            review.title = form.cleaned_data['title']
            review.comment = form.cleaned_data['comment']
            review.save()
            messages.success(request, 'Your review has been submitted.')
            return redirect('restaurant_detail', pk=restaurant.name)
        context = {'restaurant': restaurant, 'form': form}
        return render(request, 'application/review_form.html', context)
    
    def test_func(self):
        return self.request.user.is_authenticated
    
class RestaurantDetailView(FormView):
    template_name = 'application/restaurant.html'
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant = Restaurants.objects.get(name=self.kwargs['pk'])
        context['restaurant_data'] = restaurant
        context['review_data'] = Review.objects.filter(restaurant=restaurant)
        return context

    def form_valid(self, form):
        restaurant = Restaurants.objects.get(name=self.kwargs['pk'])
        review = form.save(commit=False)
        review.restaurant = restaurant
        review.author = self.request.user
        review.save()
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_success_url(self):
        restaurant = Restaurants.objects.get(name=self.kwargs['pk'])
        return reverse('restaurant_detail', kwargs={'pk': restaurant.pk})