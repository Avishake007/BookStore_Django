# Generated by Django 3.2.7 on 2022-08-06 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_bookschema_incart'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookschema',
            name='description',
            field=models.TextField(blank=True, max_length=30, null=True),
        ),
    ]
