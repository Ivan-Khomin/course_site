from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Category, Course
from .forms import SearchForm


def course_list(request, category_id=None):
    search_form = SearchForm()

    if category_id:
        object_list = Course.objects.filter(status='open', category__id=category_id)
    else:
        object_list = Course.objects.filter(status='open')

    if 'query' in request.GET:
        search_form = SearchForm(request.GET)
        if search_form.is_valid():
            query = search_form.cleaned_data['query']
            try:
                if category_id:
                    object_list = Course.objects.filter(status='open', category__id=category_id, title__contains=query)
                else:
                    object_list = Course.objects.filter(status='open', title__contains=query)
            except Exception:
                object_list = None

    categories = Category.objects.all()
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    context = {
        'courses': courses,
        'categories': categories,
        'search_form': search_form
    }

    return render(request, 'courses/course/list.html', context)


def course_detail(request, course_slug, course_id):
    course = get_object_or_404(Course, slug=course_slug, id=course_id)
    context = {'course': course}

    return render(request, 'courses/course/detail.html', context)
