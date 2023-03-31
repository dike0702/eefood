# Generated by Django 4.1.6 on 2023-03-31 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_remove_reservation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.IntegerField(choices=[(1, '10am'), (2, '11am'), (3, '12pm'), (4, '1pm'), (5, '2pm'), (6, '3pm'), (7, '5pm'), (8, '6pm'), (9, '7pm'), (10, '8pm'), (11, '9pm')], default='1', verbose_name='time'),
        ),
    ]
