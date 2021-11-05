from django.urls import path
from carprice import views

urlpatterns = [
    path('',views.carpriceHome,name='carpricehome'),
    path('carpriceprediction/', views.carpriceprediction,name='carpriceprediction'),

]