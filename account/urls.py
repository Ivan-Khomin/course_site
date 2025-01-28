from django.urls import path

from . import views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('disable-account/', views.disable_account, name='disable_account'),
    path('invalid-login/', views.invalid_login, name='invalid_login'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('edit-profile/', views.edit_profile, name='edit_profile')
]
