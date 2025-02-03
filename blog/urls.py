from django.urls import path
from django.contrib import admin

from .views import *

urlpatterns = [
    path('', get_many_blog, name='get_all'),
    path('sort/like', sort_by_like, name='like_sort'),
    path('sort/date', sort_by_date, name='data_sort'),
    path('post/', post_blog, name='post_blog_'),
    path('find/' , get_one_blog , name = 'get_one'),
    path('delete/' , delete_blog , name = 'delete'),
    path('delete/<int:id>/' , delete_blog , name = 'delete'),
    path('find/' , get_one_blog , name = 'get_one'),
    path('find/<int:id>/' , get_one_blog , name = 'get_one'),
    path('like/<int:id>/plus/', like_blog, name='like_blog'),
    path('like/<int:id>/minus/', unlike_blog, name='unlike_blog'),
    path('like/<int:id>/reset/', reset_likes, name='reset_likes'),
    path('edit/<int:id>/', edit_blog, name='edit_blog'),
    path('title/<str:title>/', get_one_blog_title, name='get_one_blog_title'),
    path('text/<str:input_text>/', get_similar_blogs, name='get_similar_blogs'),
    
]