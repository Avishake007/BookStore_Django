# Generated by Django 4.0.6 on 2022-08-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_user_userschema'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookSchema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('author', models.CharField(max_length=122)),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserSchema',
        ),
    ]
