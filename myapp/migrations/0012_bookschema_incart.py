# Generated by Django 3.2.7 on 2022-08-06 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_bookschema_book_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookschema',
            name='inCart',
            field=models.BooleanField(default=False),
        ),
    ]
