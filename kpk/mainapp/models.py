from django.db import models


class SubjectCategory(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление подготовки'
        verbose_name_plural = 'Направления подготовки'


class Course(models.Model):
    EASY = 'e'
    MEDIUM = 'm'
    HARD = 'h'
    LEVEL_CHOICES = (
        (EASY, 'легкий'),
        (MEDIUM, 'средний'),
        (HARD, 'продвинутый'),
    )

    category = models.ForeignKey(SubjectCategory,
                                 on_delete=models.CASCADE)
    # slug = models.SlugField()  # name -> some function -> slug
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)
    hours = models.IntegerField(default=0)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, default=EASY)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
