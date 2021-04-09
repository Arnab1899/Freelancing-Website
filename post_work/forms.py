from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User

from post_work.models import PostWork


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
        model = PostWork
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
