# Generated by Django 3.2.9 on 2023-04-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_reservation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='business_hours',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
