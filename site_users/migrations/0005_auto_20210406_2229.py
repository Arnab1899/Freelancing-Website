# Generated by Django 3.1.7 on 2021-04-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_users', '0004_auto_20210405_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
