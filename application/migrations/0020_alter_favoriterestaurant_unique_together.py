# Generated by Django 3.2.9 on 2023-04-13 05:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('application', '0019_favoriterestaurant'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favoriterestaurant',
            unique_together={('user', 'restaurant')},
        ),
    ]
