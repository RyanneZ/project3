# Generated by Django 4.0.5 on 2022-06-28 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_profile_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='about',
        ),
    ]
