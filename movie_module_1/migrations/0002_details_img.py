# Generated by Django 3.2.7 on 2021-09-20 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_module_1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='img',
            field=models.ImageField(blank=True, upload_to='media/upoads'),
        ),
    ]
