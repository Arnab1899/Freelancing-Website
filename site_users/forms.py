from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


class UseRegistrationForm(UserCreationForm):
    First_name = forms.CharField()
    Last_name = forms.CharField()
    email = forms.EmailField()
    Phone_Number = forms.IntegerField()
    Profession = forms.CharField()
    Age = forms.IntegerField()
    Address = forms.CharField()

    class Meta:
        model = User
        fields = ['username',
                  'First_name',
                  'Last_name',
                  'email',
                  'Phone_Number',
                  'password1',
                  'password2',
                  'Profession',
                  'Age',
                  'Address',
                  ]






