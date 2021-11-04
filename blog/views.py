# Create your views here.
from blog.models import Blog
from django.shortcuts import render,redirect
from datetime import datetime
from myprojects.models import Project
# from django.contrib import messages
# from django.core.paginator import Paginator
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from .decorators import admin_only
from django.http import Http404
from django.http import HttpResponse
# from .models import *
# Create your views here.

def blogs(request):
    blogs=Blog.objects.all()
    i1='sun, girl'
    return render(request,"blog/blogmodel.html",{'blogs':blogs})


def blog(request,slug):
	blog=Blog.objects.get(slug=slug)
	blogs=Blog.objects.all()
	i1='sun, girl'
	return render(request,"blog/blogmodel1.html",{'blog':blog,'blogs':blogs})

# #CRUD VIEWS
@admin_only
@login_required(login_url="account/login")
def createBlog(request):
	form = BlogForm()
	
	if request.method == 'POST':
		form = BlogForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('blogs')

	context = {'form':form}
	return render(request, 'blog/blog_form.html', context)

def fuck(request):
	return render(request, 'blog/delete.html')
	


@admin_only
@login_required(login_url="account/login")
def updateBlog(request, slug):
	post = Blog.objects.get(slug=slug)
	form = BlogForm(instance=post)
	try:
		if request.method == 'POST':
			form = BlogForm(request.POST, request.FILES, instance=post)
			if form.is_valid():
				form.save()
			return redirect('blogs')
	except Blog.DoesNotExist:
		return Http404("Post does not exist")

	context = {'form':form}
	return render(request, 'blog/blog_form.html', context)


@admin_only
@login_required(login_url="account/login")
def deleteBlog(request, slug):
	post = Blog.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('blogs')
	context = {'item':post}
	return render(request, 'blog/delete.html', context)

