from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Restaurants(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        primary_key=True
    )
    addr = models.CharField(
        max_length=300,
        blank=False,
        null=False
    )
    table = models.PositiveSmallIntegerField(
        blank=False,
        null=False,
    )
    Genre = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    phone = PhoneNumberField(
        blank=False,
        null=False
    )
    img = models.ImageField(
        blank=True,
        upload_to='media/'
    )

    def __str__(self):
        return self.name

TIME_SCHEDULE = [
    (1, '10am'),
    (2, '11am'),
    (3, '12pm'),
    (4, '1pm'),
    (5, '2pm'),
    (6, '3pm'),
    (7, '5pm'),
    (8, '6pm'),
    (9, '7pm'),
    (10, '8pm'),
    (11, '9pm'),
]

class Reservation(models.Model):
    restaurant = models.ForeignKey(
        Restaurants, 
        on_delete=models.CASCADE
    )
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        null=True
    )
    date = models.DateField(
        blank=False,
    )
    time = models.IntegerField(
        verbose_name='time', 
        choices=TIME_SCHEDULE, 
        default='1'
    )
    num_people = models.IntegerField(
        blank=False,
    )

    def __str__(self):
        return str(self.name)
    
SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]
    
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name='reviews', null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title =models.CharField("Title", max_length=255)
    comment =models.TextField("Comment", max_length=255)
    rate = models.IntegerField(verbose_name='レビュースコア', choices=SCORE_CHOICES, default='3')
    image = models.ImageField(upload_to='review_images', null=True, blank=True)
    created = models.DateTimeField("Date", default=timezone.now)
        
    def __str__(self):
            return str(self.author)
        