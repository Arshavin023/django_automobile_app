# Generated by Django 5.0.2 on 2024-02-22 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
