import authapp.views as authapp
from django.urls import path

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('profile/edit/', authapp.edit_profile, name='edit_profile'),
]
