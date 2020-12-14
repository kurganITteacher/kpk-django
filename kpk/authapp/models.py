from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True)
    about = models.TextField(verbose_name='о себе', blank=True)
