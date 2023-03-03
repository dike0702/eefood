from django.contrib import admin
from .models import Restaurants
from .models import Review

admin.site.register(Restaurants)
admin.site.register(Review)