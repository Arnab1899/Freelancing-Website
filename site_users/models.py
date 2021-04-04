from django.db import models
from django.contrib.auth.models import User


class SiteUsers(models.Model):
    User_Name = models.TextField(primary_key=True, db_column='User Name')
    First_Name = models.CharField(max_length=30, db_column='First Name')
    Last_Name = models.CharField(max_length=30, db_column='Last Name')
    Email = models.EmailField(max_length=20, db_column='Email')
    Phone_Number = models.IntegerField(db_column='Phone Number')
    Password = models.CharField(db_column='Password', max_length=50)
    Profession = models.CharField(max_length=30, db_column='Profession')
    Age = models.IntegerField(db_column='Age')
    Address = models.CharField(max_length=100, db_column='Address')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    phone = models.IntegerField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_picture')

    def __str__(self):
        return self.user.username


