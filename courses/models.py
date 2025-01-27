from django.db import models
from django.urls import reverse
from django.utils.timezone import now

COURSE_STATUS = {
    ('open', 'Open'),
    ('closed', 'Closed')
}


class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name='Назва')
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ['-title']
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=250, verbose_name='Назва')
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='Категорія'
    )
    description = models.TextField(verbose_name='Опис')
    start_date = models.DateTimeField(default=now, verbose_name='Дата початку')
    finish_date = models.DateTimeField(default=now, verbose_name='Дата закінчення')
    number_of_lecture = models.PositiveIntegerField(verbose_name='Кількість лекцій')
    status = models.CharField(max_length=10, choices=COURSE_STATUS, verbose_name='Статус')

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курси'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:course_detail', args=[
            self.slug,
            self.id
        ])

