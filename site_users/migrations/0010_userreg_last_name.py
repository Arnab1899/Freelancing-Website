# Generated by Django 3.1.7 on 2021-04-07 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_users', '0009_userreg'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='last_name',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
