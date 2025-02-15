# Generated by Django 5.0.7 on 2024-07-23 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='review',
        ),
    ]
