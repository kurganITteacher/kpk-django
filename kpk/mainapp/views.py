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


def catalog_section(request, category_pk):
    courses = Course.objects.filter(category_id=category_pk)
    context = {
        'courses': courses,
        'page_title': 'страница каталога'
    }
    return render(request, 'mainapp/catalog_page.html', context)


def course_page(request, course_pk):
    course = Course.objects.get(pk=course_pk)
    context = {
        'course': course,
        'page_title': 'страница курса'
    }
    return render(request, 'mainapp/course_page.html', context)
