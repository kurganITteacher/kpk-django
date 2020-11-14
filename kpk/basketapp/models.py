from django.contrib.auth.models import User
from django.db import models

from mainapp.models import Course


class CourseBasket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
