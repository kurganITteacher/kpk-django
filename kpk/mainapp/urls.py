import mainapp.views as mainapp
from django.urls import path

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('catalog/', mainapp.catalog, name='catalog'),

    path('catalog/category/<int:category_pk>/', mainapp.catalog_section, name='catalog_section'),
    path('catalog/course/<int:course_pk>/', mainapp.course_page, name='course_page'),

]
