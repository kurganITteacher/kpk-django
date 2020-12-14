from basketapp.models import CourseBasket
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from mainapp.models import Course


@login_required
def index(request):
    items = CourseBasket.objects.filter(user=request.user)
    context = {
        'object_list': items,
    }

    return render(request, 'basketapp/basket.html', context)


# @login_required
# def basket_detailed(request):
#     items = CourseBasket.objects.filter(user=request.user)
#     context = {
#         'object_list': items,
#     }
#
#     return render(request, 'basketapp/basket_detailed.html', context)


@login_required
def add(request, course_id):
    course = Course.objects.get(pk=course_id)
    CourseBasket.objects.get_or_create(
        user=request.user,
        course=course
    )
    return HttpResponseRedirect(
        reverse('mainapp:catalog_section',
                kwargs={'category_pk': course.category_id})
    )


@login_required
def remove(request, course_basket_id):
    if request.is_ajax():
        item = CourseBasket.objects.get(id=course_basket_id)
        item.delete()
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return JsonResponse({'status': 'ok',
                             'course_basket_id': course_basket_id})
