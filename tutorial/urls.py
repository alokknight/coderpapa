from django.contrib import admin
from django.urls import path
from tutorial import views

urlpatterns = [
    # #tutorial
    path('tut/<slug:slug>/',views.showTutorial,name='show_tut'),
    path('',views.showAllTutorial,name='show_all_tut'),
    # path('tutorial/',views.create_tut,name='create_tut'),
    # path('update_tut/<slug:slug>/',views.updatetut, name='update_tut'),
    # path('delete_tut/<slug:slug>/',views.deletetut, name='delete_tut'),
    # path('<slug:slug>/',views.tut, name='slug'),
]