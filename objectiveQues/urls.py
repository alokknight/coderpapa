from django.contrib import admin
from django.urls import path
from objectiveQues import views
# from optionalques.urls import views
#from app1 import views
urlpatterns = [
    path('',views.q, name='ques'),
    path('<str:subject>/',views.view_subject_questions,name='view_subject_questions')

]