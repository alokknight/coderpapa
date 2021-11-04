from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('',views.blogs,name='blogs'),

    path('create_blog/',views.createBlog,name='create_blog'),
    path('update_blog/<slug:slug>/',views.updateBlog, name='update_blog'),
    path('delete_blog/<slug:slug>/',views.deleteBlog, name='delete_blog'),
    path('<slug:slug>/',views.blog, name='slug'),


]
