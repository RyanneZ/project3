# Generated by Django 4.0.5 on 2022-06-27 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='description',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
