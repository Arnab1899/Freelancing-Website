from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User
from .models import Profile


class UseRegistrationForm(UserCreationForm):
    First_name = forms.CharField()
    Last_name = forms.CharField()
    email = forms.EmailField()
    Phone_Number = forms.CharField()
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


class UserJobSetForm(UserCreationForm):
    Job_Name = forms.CharField()
    Job_Type = forms.CharField()
    Job_Description = forms.CharField()
    Job_Requirements = forms.CharField()
    Job_Experience = forms.CharField()
    Job_Salary = forms.IntegerField()
    Job_Location = forms.CharField()

    class Meta:
        model = User
        fields = ['Job_Name',
                  'Job_Type',
                  'Job_Description',
                  'Job_Requirements',
                  'Job_Experience',
                  'Job_Salary',
                  'Job_Location',
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
            'phone',
            'profile_picture',
        ]






