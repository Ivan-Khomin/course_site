# Generated by Django 5.1.5 on 2025-01-27 10:30

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=250)),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=250)),
                ('description', models.TextField(verbose_name='Опис')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата початку')),
                ('finish_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата закінчення')),
                ('number_of_lecture', models.PositiveIntegerField(verbose_name='Кількість лекцій')),
                ('status', models.CharField(choices=[('closed', 'Closed'), ('open', 'Open')], max_length=10, verbose_name='Статус')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курси',
                'ordering': ['-start_date'],
            },
        ),
    ]
