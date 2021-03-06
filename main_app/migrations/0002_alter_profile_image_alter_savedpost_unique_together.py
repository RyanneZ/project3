# Generated by Django 4.0.5 on 2022-07-09 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterUniqueTogether(
            name='savedpost',
            unique_together={('user', 'post')},
        ),
    ]
