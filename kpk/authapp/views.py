import django.contrib.auth as auth
from authapp.forms import ChangeForm
from authapp.forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = LoginForm()

    context = {
        'page_title': 'авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        form = RegisterForm()

    context = {
        'page_title': 'регистрация',
        'form': form,
    }
    return render(request, 'authapp/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST, request.FILES, instance=request.user)
        # profile_form = ProfileChangeForm(request.POST, request.FILES, instance=request.user)
        # if form.is_valid() and profile_form.is_valid():
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:edit_profile'))
    else:
        form = ChangeForm(instance=request.user)

    context = {
        'page_title': 'редактирование',
        'form': form,
    }
    return render(request, 'authapp/edit.html', context)
