from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


class UseRegistrationForm(UserCreationForm):
    First_name = forms.EmailField()
    Last_name = forms.EmailField()
    email = forms.EmailField()
    Phone_Number = forms.EmailField()
    Profession = forms.EmailField()
    Age = forms.EmailField()
    Address = forms.EmailField()

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






