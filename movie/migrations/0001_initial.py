# Generated by Django 5.0.7 on 2024-07-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviedatabase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
