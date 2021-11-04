from django.shortcuts import render, HttpResponse,redirect
from django.http import HttpResponse
from datetime import datetime
from main.models import Contact, Tutorial, FrontPage, Crausal
from django.contrib import messages


def index(request):
    # contests=Contest.objects.all()
    front=FrontPage.objects.all()
    carousels=Crausal.objects.all()
    return render(request, 'main/index.html',{'front':front,'carousels':carousels})


def tutindex(request):
    tuts=Tutorial.objects.all()
    return render(request,'main/tutindex.html', {'tuts':tuts} )


# # #CRUD VIEWS
# @admin_only
# @login_required(login_url="account/login")
# def createBlog(request):
# 	form = BlogForm()
	
# 	if request.method == 'POST':
# 		form = BlogForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 		return redirect('blogs')

# 	context = {'form':form}
# 	return render(request, 'blog/blog_form.html', context)

# def fuck(request):
# 	return render(request, 'blog/delete.html')
	


# @admin_only
# @login_required(login_url="account/login")
# def updateBlog(request, slug):
# 	post = Tutorial.objects.get(slug=slug)
# 	form = BlogForm(instance=post)
# 	try:
# 		if request.method == 'POST':
# 			form = BlogForm(request.POST, request.FILES, instance=post)
# 			if form.is_valid():
# 				form.save()
# 			return redirect('blogs')
# 	except Tutorial.DoesNotExist:
# 		return Http404("Post does not exist")

# 	context = {'form':form}
# 	return render(request, 'blog/blog_form.html', context)


# @admin_only
# @login_required(login_url="account/login")
# def deleteBlog(request, slug):
# 	post = Tutorial.objects.get(slug=slug)

# 	if request.method == 'POST':
# 		post.delete()
# 		return redirect('blogs')
# 	context = {'item':post}
# 	return render(request, 'blog/delete.html', context)





def about(request):
    return render(request, 'main/about.html')

def services(request):
    services= Tutorial.objects.all()
    return render(request, 'main/services.html',{'services':services})

def contact(request):
    if  request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get("phone")
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "your message have been sent...!!")
    return render(request, 'main/contact.html')
    #return HttpResponse("this is contact page")

def projects(request):
    return render(request,'main/projects.html')
