from django.db import models


class SiteUsers(models.Model):
    User_Name = models.TextField(primary_key=True, db_column='User Name')
    First_Name = models.CharField(max_length=30, db_column='First Name')
    Last_Name = models.CharField(max_length=30, db_column='Last Name')
    Email = models.EmailField(max_length=20, db_column='Email')
    Phone_Number = models.IntegerField(db_column='Phone Number')
    Password = models.CharField(db_column='Password', max_length=50)
    Password_confirmation = models.CharField(max_length=50, db_column='Password Confirmation')
    Profession = models.CharField(max_length=30, db_column='Profession')
    Age = models.IntegerField(db_column='Age')
    Address = models.CharField(max_length=100, db_column='Address')
