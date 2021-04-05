from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Profile


class UseRegistrationForm(UserCreationForm):
    First_name = forms.CharField()
    Last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',
                  'First_name',
                  'Last_name',
                  'email',
                  'password1',
                  'password2',
                  ]


class UserJobSetForm(forms.ModelForm):
    Company_Name = forms.CharField()
    Title = forms.CharField()
    Work_Type = forms.CharField()
    Description = forms.CharField()
    Requirements = forms.CharField()
    Experience = forms.CharField(required=False)
    Salary = forms.IntegerField()
    Location = forms.CharField(required=False)
    Vacancy = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
                  'Company_Name',
                  'Title',
                  'Work_Type',
                  'Description',
                  'Requirements',
                  'Experience',
                  'Salary',
                  'Location',
                  'Vacancy',
                  ]


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',

        ]


class ProfileUpdateFrom(forms.ModelForm):
    phone = forms.CharField(max_length=15, required=False)
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = [
            'age',
            'profession',
            'address',
            'phone',
            'profile_picture',
        ]






