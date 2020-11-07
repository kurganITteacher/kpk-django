from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from authapp.forms import LoginForm


def login(request):
    # form = AuthenticationForm()
    form = LoginForm()

    context = {
        'page_title': 'авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)
