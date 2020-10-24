from django.shortcuts import render

from mainapp.models import SubjectCategory, Course


def index(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    categories = SubjectCategory.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }

    return render(request, 'mainapp/catalog.html', context)


def basket(request):
    return render(request, 'mainapp/basket.html')


def catalog_page(request, pk):
    # catalog/category/<int:pk>/
    # catalog/mobile/notebooks/1210762/ => 1210762 - pk
    # https://www.citilink.ru/catalog/mobile/notebooks/1210762/ => 1210762 - pk
    # catalog/category/<str:slug>/
    # catalog/17a89aab16404e77/videokarty/ => videokarty - slug
    # https://www.dns-shop.ru/catalog/17a89aab16404e77/videokarty/ => videokarty - slug
    # items = SubjectCategory.objects.all()
    # courses = Course.objects.filter(category__slug=slug)  # WHERE ...
    courses = Course.objects.filter(category_id=pk)
    context = {
        'courses': courses,
        'page_title': 'страница каталога'
    }
    return render(request, 'mainapp/catalog_page.html', context)
