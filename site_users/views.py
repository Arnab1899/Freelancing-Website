from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UseRegistrationForm
from .forms import UserJobSetForm, UserUpdateForm, ProfileUpdateFrom
from django.contrib.auth.decorators import login_required


def base(request):
    return render(request, 'users/base.html')


def profile(request):
    return render(request, 'users/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateFrom(request.POST,
                                                request.FILES,
                                                instance=request.user.profile)

        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()

            return redirect('profile')
        else:
            context = {
                'user_update_form': user_update_form,
                'profile_update_form': profile_update_form

            }
            return render(request, 'users/profile_update.html', context)
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateFrom()

        context = {
            'user_update_form': user_update_form,
            'profile_update_form': profile_update_form
        }
        return render(request, 'users/profile_update.html', context)


def about(request):
    return render(request, 'users/about.html')


def contract(request):
    return render(request, 'users/contract.html')


def register_admin(request):
    if request.method == "POST":
        registration_form = UserJobSetForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('login')
        else:
            context = {
                'form': registration_form
            }
            return render(request, 'users/register_admin.html', context)

    else:
        registration_form = UseRegistrationForm()
        context = {
            'form': registration_form
        }

        return render(request, 'users/register_admin.html', context)


def job_set(request):
    if request.method == "POST":
        set_form = UserJobSetForm(request.POST)
        if set_form.is_valid():
            set_form.save()
            return redirect('work')
        else:
            set_form = UserJobSetForm()
            context = {
                'form': set_form
            }
            return render(request, 'users/job_set.html', context)

    else:
        set_form = UserJobSetForm()
        context = {
            'form': set_form
        }
        return render(request, 'users/job_set.html', context)


@login_required
def find_work(request):
    return render(request, 'users/find_work.html')








