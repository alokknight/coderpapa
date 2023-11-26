from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Project


# class CustomUserCreationForm(UserCreationForm):

# 	class Meta:
# 		model = User
# 		fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class ProjectForm(ModelForm):

	class Meta:
		model = Project
		fields = '__all__'
