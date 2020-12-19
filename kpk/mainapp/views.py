from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import SubjectCategory, Course


# def index(request):
#     return render(request, 'mainapp/index.html')


# # FBV - Function Based Views
# def catalog(request):
#     categories = SubjectCategory.objects.all()
#     categories = SubjectCategory.objects.filter(is_active=True)
#     context = {
#         'categories': categories,
#         'page_title': 'каталог'
#     }
#
#     return render(request, 'mainapp/catalog.html', context)
pass

# Class Based Views
# tmplate name -> class name + suffix
# tmplate name -> subjectcategory_list
# mainapp/subjectcategory_list.html
# class CatalogListView(ListView):
#     model = SubjectCategory
#     # context_object_name = 'categories'
#     # template_name = 'mainapp/catalog.html'
#
#     # def get_context_data(self, *, object_list=None, **kwargs):
#     #     context = super().get_context_data(object_list, **kwargs)
#     #     context['second_list'] = pass
#     #     return context
#
#     # def get_queryset(self):
#     #     return self.model.objects.filter(is_active=True)
pass


# class CatalogListView(ListView):
#     model = SubjectCategory
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['page_title'] = 'каталог'
#         # print('context', context)
#         return context

class PageTitleMixin:
    page_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = self.page_title
        return context


class CatalogListView(PageTitleMixin, ListView):
    model = SubjectCategory
    page_title = 'каталог'


# 'locationsapp/locations_list.html'
# class LocationsListView(ListView):
#     model = Locations
#     page_title = 'локации'
#
#
# class ManagersListView(PageTitleMixin, ListView):
#     model = Managers
#     page_title = 'менеджеры'


# DetailView -> object, category_pk -> pk
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
