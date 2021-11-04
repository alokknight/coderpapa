from django.contrib import admin
from django.urls import path
from wineshop import views
urlpatterns = [
    path('',views.wineshop,name='wineshop'),

]
