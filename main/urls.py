from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('services/',views.services,name='services'),
    path('contact/',views.contact,name='contact'),
    # path('tutorial/', views.tutindex, name ='tutindex'),

    # #tutorial
    # path('create_tut/',views.createtut,name='create_tut'),
    # path('update_tut/<slug:slug>/',views.updatetut, name='update_tut'),
    # path('delete_tut/<slug:slug>/',views.deletetut, name='delete_tut'),
    # path('<slug:slug>/',views.tut, name='slug'),



]
