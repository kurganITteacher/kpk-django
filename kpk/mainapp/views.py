from django.shortcuts import render

from mainapp.models import SubjectCategory


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = SubjectCategory.objects.all()
    context = {
        'categories': categories
    }

    return render(request, 'mainapp/catalog.html', context)


def basket(request):
    return render(request, 'mainapp/basket.html')
