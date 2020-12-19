import mainapp.views as mainapp
from django.urls import path
from django.views.generic import TemplateView

app_name = 'mainapp'

urlpatterns = [
    # path('', mainapp.index, name='index'),
    path('', TemplateView.as_view(template_name='mainapp/index.html'), name='index'),

    # path('catalog/', mainapp.catalog, name='catalog'),
    path('catalog/', mainapp.CatalogListView.as_view(), name='catalog'),

    path('catalog/category/<int:category_pk>/', mainapp.catalog_section, name='catalog_section'),
    path('catalog/course/<int:course_pk>/', mainapp.course_page, name='course_page'),

]
