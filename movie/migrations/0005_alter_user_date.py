# Generated by Django 5.0.7 on 2024-07-24 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 24, 4, 3, 54, 776956, tzinfo=datetime.timezone.utc)),
        ),
    ]
