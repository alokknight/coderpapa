from django.contrib import admin
from django.urls import path, include
from account import views
#from app1 import views
urlpatterns = [
    # path('',views.index, name='index'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('login/',views.login_, name='login'),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_, name='logout'),
    # path('profile/',views.profile,name='profile'),

]
