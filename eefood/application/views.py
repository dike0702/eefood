from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .models import Restaurants, Review, Reservation
from django.contrib import messages
from .forms import ReviewForm, PostRestaurantForm, ReservationForm, RestaurantSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from django.db.models import Avg, Q

class IndexView(ListView):
    template_name = 'application/index.html'
    context_object_name = 'restaurant_data'
    paginate_by = 10

    def get_queryset(self):
        query_name = self.request.GET.get('name')
        query_genre = self.request.GET.get('genre')

        if query_name and query_genre:
            qs = Restaurants.objects.filter(name__icontains=query_name, Genre__icontains=query_genre)
        elif query_name:
            qs = Restaurants.objects.filter(name__icontains=query_name)
        elif query_genre:
            qs = Restaurants.objects.filter(Genre__icontains=query_genre)
        else:
            qs = Restaurants.objects.all()

        return qs

class ItemDetailView(View):
    def get(self, request, *args, **kwargs):
        restaurant_data = Restaurants.objects.get(name=self.kwargs['name'])
        review_data = Review.objects.order_by('-id')
        avg_rate = Review.objects.filter(restaurant=restaurant_data).aggregate(avg_rate=Avg('rate'))
        if avg_rate['avg_rate'] is not None:
            avg_rate_round = round(avg_rate['avg_rate'], 1)
            avg_rate_stars = int(avg_rate_round)
        else:
            avg_rate_round = None
            avg_rate_stars = None
        return render(request, 'application/restaurant.html', {
            'restaurant_data': restaurant_data,
            'review_data': review_data,
            'avg_rate_round': avg_rate_round,
            'avg_rate_stars': avg_rate_stars
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
                reservation.name = request.user
                reservation.save()
                return redirect('top')
        else:
            form = PostRestaurantForm()
            restaurant_data = Restaurants.objects.get(name=self.kwargs['name'])
        return render(request, 'reservation_create.html', {
            'form': form, 
            'restaurant': restaurant_data
        })

class ReservationDetailView(View):
    model = Reservation
    template_name = 'reservation_detail.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return super().get_queryset().filter(name=self.request.user)

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
        
        else:
            messages.error(request, 'There was an error submitting your review.')
        context = {'restaurant': restaurant, 'form': form}
        return render(request, 'application/review_form.html', context)
        # context = {'restaurant': restaurant, 'form': form}
        # return render(request, 'application/review_form.html', context)
    
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
    
class ReviewEditView(LoginRequiredMixin, UpdateView):
    model = Review
    fields = ['title', 'comment', 'rate']
    template_name = 'application/review_edit.html'
    success_url = reverse_lazy('top')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != self.request.user:
            return HttpResponseForbidden()
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.restaurant = self.object.restaurant
        return super().form_valid(form)
    
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'application/review_delete.html'
    success_url = reverse_lazy('top')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            return HttpResponseForbidden()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)