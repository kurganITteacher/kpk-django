from django.db import models


class SubjectCategory(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(SubjectCategory,
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    hours = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# 5 category
# 8 items
# 5 + 40 = 45 items
# 12:30
