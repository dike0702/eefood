from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# class Category(models.Model):
#     name = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False,
#         unique=True)
    
#     def __str__(self):
#         return self.name


# class Tag(models.Model):
#     name = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False,
#         unique=True)
    
#     def __str__(self):
#         return self.name


# class Post(models.Model):
#     created = models.DateTimeField(
#         auto_now_add=True,
#         editable=False,
#         blank=False,
#         null=False)
    
#     updated = models.DateTimeField(
#         auto_now=True,
#         editable=False,
#         blank=False,
#         null=False)
        
#     title = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False)
        
#     body = models.TextField(
#         blank=True,
#         null=False)
        
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE)
        
#     tags = models.ManyToManyField(
#         Tag,
#         blank=True)

#     def __str__(self):
#         return self.title

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
        upload_to='images/'
    )

    def __str__(self):
        return self.name
    
SCORE_CHOICES = [
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
]
    
class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title =models.CharField("Title", max_length=255)
    comment =models.TextField("Comment", max_length=255)
    rate = models.IntegerField(verbose_name='レビュースコア', choices=SCORE_CHOICES, default='3')
    created = models.DateTimeField("Date", default=timezone.now)
        
    def __str__(self):
            return str(self.user)
        