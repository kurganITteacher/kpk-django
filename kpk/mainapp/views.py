from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    return render(request, 'mainapp/catalog.html')


def basket(request):
    return render(request, 'mainapp/basket.html')
