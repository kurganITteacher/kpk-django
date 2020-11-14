import basketapp.views as basketapp
from django.urls import path

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
]
