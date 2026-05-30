
from django.urls import path

from .views.main_view import create_blog, edit_blog, single_blog, home,delete_blog,about_blog,contact_blog
from .views.auth_view import loginuser, register

urlpatterns = [
    path("", home, name='home'),
    path("register/", register, name='register'),
    path("login/", loginuser, name='login'),
    path("create/", create_blog, name='create_blog'),
    path("<int:blog_id>/edit", edit_blog, name='edit_blog'),
    path("<int:blog_id>/", single_blog, name='single_blog'),
    path("<int:blog_id>/delete",delete_blog, name='delete_blog'),
    path("about/", about_blog, name='about_blog'),
    path("contact/",contact_blog,name='contact_blog'),

]