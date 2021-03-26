from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UseRegistrationForm


def base(request):
    return render(request, 'users/base.html')


def register(request):
    if request.method == "POST":
        registration_form = UseRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('first-page')

    else:
        registration_form = UseRegistrationForm()
        context = {
            'form': registration_form
        }

        return render(request, 'users/register.html', context)


def register_admin(request):
    if request.method == "POST":
        registration_form = UseRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('first-page')

    else:
        registration_form = UseRegistrationForm()
        context = {
            'form': registration_form
        }

        return render(request, 'users/register_admin.html', context)





