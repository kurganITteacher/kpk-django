import django.contrib.auth as auth
from django.http import HttpResponseRedirect
from django.shortcuts import render

from authapp.forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    context = {
        'page_title': 'авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)
