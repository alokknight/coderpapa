from django.shortcuts import render,redirect
from myprojects.models import Project
from django.core.paginator import Paginator
from .forms import  ProjectForm
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import admin_only

# Create your views here.
def projects(request):
    projects=Project.objects.all()
    # paginator = Paginator(projects, 2) # Show 2 Project per page.

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    return render(request, 'myprojects/projects.html',{'projects':projects})#,'page_obj':page_obj})

def viewProject(request,slug):
    project=Project.objects.get(slug=slug)
    related_skills = project.techused.all()
    # paginator = Paginator(projects, 2) # Show 2 Project per page.

    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    return render(request, 'myprojects/project.html',{'project':project,'related_skills':related_skills})#,'page_obj':page_obj})




#CRUD VIEWS
@admin_only
@login_required(login_url="account/login")
def createProject(request):
	form = ProjectForm()

	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('projects')

	context = {'form':form}
	return render(request, 'myprojects/project_form.html', context)


@admin_only
@login_required(login_url="account/login")
def updateProject(request, slug):
	post = Project.objects.get(slug=slug)
	form = ProjectForm(instance=post)

	if request.method == 'POST':
		form = ProjectForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('projects')

	context = {'form':form}
	return render(request, 'myprojects/project_form.html', context)

@admin_only
@login_required(login_url="account/login")
def deleteProject(request, slug):
	post = Project.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('projects')
	context = {'item':post}
	return render(request, 'myprojects/delete.html', context)

