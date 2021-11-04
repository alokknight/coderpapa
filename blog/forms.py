from django import forms
from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from .models import Blog

class BlogForm(ModelForm):

	class Meta:
		model = Blog
		fields = '__all__'
