
from django.urls import path

from .views.main_view import create_blog, edit_blog, single_blog, home
from .views.auth_view import login, register

urlpatterns = [
    path("", home, name='home'),
    path("register/", register, name='register'),
    path("login/", login, name='login'),
    path("create/", create_blog, name='create_blog'),
    path("edit/", edit_blog, name='edit_blog'),
    path("single/", single_blog, name='single_blog'),

]