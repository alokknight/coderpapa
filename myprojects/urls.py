from django.contrib import admin
from django.urls import path
from myprojects import views
#from app1 import views
urlpatterns = [
    path('',views.projects, name='projects'),
    path('create_projects/',views.createProject,name='create_projects'),
    path('update_projects/<slug:slug>/',views.updateProject, name='update_projects'),
    path('delete_projects/<slug:slug>/',views.deleteProject, name='delete_projects'),
    path('<slug:slug>/',views.viewProject, name='project'),
    
]