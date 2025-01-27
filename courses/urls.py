from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:category_id>/', views.course_list, name='course_list_by_category'),
    path('<slug:course_slug>/<int:course_id>/', views.course_detail, name='course_detail')
]
