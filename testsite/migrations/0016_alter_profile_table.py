# Generated by Django 4.2 on 2024-02-29 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testsite', '0015_profile_groups'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='profile',
            table='user',
        ),
    ]
