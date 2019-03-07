from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import (
                    RegistrationForm,
                    EditProfileForm,
                )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash # User is still login even after password change redirect
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        # form = UserCreationForm()
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/register.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        # form = UserChangeForm(request.POST, instance=request.user) # Passing the user instance so it knows user object
        form = EditProfileForm(request.POST, instance=request.user) # Passing the user instance so it knows user object
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        # form = UserChangeForm(instance=request.user)
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required(login_url = '/account/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user) # Passing the user instance so it knows user object here keyword is user instead of instance.
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) # Not request.user beause we want the user who was using the form.
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
