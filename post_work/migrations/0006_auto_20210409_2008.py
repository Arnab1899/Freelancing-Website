# Generated by Django 3.1.7 on 2021-04-09 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_users', '0015_auto_20210408_1431'),
        ('post_work', '0005_auto_20210409_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postwork',
            name='user',
            field=models.ForeignKey(db_column='User', default='', on_delete=django.db.models.deletion.CASCADE, to='site_users.profile'),
        ),
    ]
