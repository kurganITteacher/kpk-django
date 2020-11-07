import django.contrib.auth as auth
from authapp.forms import LoginForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            # return HttpResponseRedirect('/')
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
