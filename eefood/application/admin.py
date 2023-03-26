from django.contrib import admin
from .models import Restaurants, Review, Reservation

admin.site.register(Restaurants)
admin.site.register(Reservation)
admin.site.register(Review)