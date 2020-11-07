from django.shortcuts import render

from authapp.forms import LoginForm


def login(request):
    form = LoginForm()

    context = {
        'page_title': 'авторизация',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)
