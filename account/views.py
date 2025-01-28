from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import LoginForm, SignUpForm, EditProfileForm


@login_required
def dashboard(request):
    return render(request, 'account/dashboard/index.html')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(
                request,
                username=cleaned_data['username'],
                password=cleaned_data['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('account:dashboard')
                else:
                    return redirect('account:disable_account')
            else:
                return redirect('account:invalid_login')
    else:
        form = LoginForm()

    context = {'form': form}

    return render(request, 'account/registration/login.html', context)


@login_required
def logout_user(request):
    logout(request)

    return redirect('main:index')


def disable_account(request):
    return render(request, 'account/registration/disable_account.html')


def invalid_login(request):
    return render(request, 'account/registration/invalid_login.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            user.save()
            login(
                request,
                authenticate(
                    request,
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
            )
            return redirect('account:dashboard')
    else:
        form = SignUpForm()

    context = {'form': form}

    return render(request, 'account/registration/sign_up.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:dashboard')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}

    return render(request, 'account/dashboard/edit_profile.html', context)
