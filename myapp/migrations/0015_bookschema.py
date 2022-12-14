# Generated by Django 3.2.7 on 2022-08-06 12:19

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0014_delete_bookschema'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_img', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('name', models.CharField(max_length=122)),
                ('author', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=30)),
                ('inCart', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('userId', models.IntegerField()),
            ],
        ),
    ]
