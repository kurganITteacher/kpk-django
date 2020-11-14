from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import CourseBasket
from django.urls import reverse

from mainapp.models import Course


def index(request):
    return render(request, 'basketapp/basket.html')


def add(request, course_id):
    course = Course.objects.get(pk=course_id)
    CourseBasket.objects.get_or_create(
        user=request.user,
        # course_id=course_id
        course=course
    )
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(
        reverse('mainapp:catalog_section',
                kwargs={'category_pk': course.category_id})
    )
