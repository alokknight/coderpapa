from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .decorators import *
from account.forms import ProfileForm
from .forms import PostForm, CustomUserCreationForm, UserForm
from .filters import PostFilter
from . import filters##
from .models import *
from myprojects.models import Project
from myprojects.models import*#
from account.models import Profile
# Create your views here.

# def home(request):
# 	posts = Post.objects.filter(active=True, featured=True)[0:3]
# 	posts = Project.objects.all()[0:3]
# 	# Access the current user
# 	current_user = request.user
# 	# Access the user's profile data
# 	try:
# 		user_profile = Profile.objects.get(user=current_user)
#     except Profile.DoesNotExist:
# 		user_profile = None

# 	context = {'posts':posts,'user_profile':user_profile}

# 	return render(request, 'portfolio/index.html',context)
# 	# return HttpResponse('<h1>aaaaaaaa</h1>')

def home(request):
	posts = Post.objects.filter(active=True, featured=True)[0:3]
	current_user = request.user
	try:
		user_profile = Profile.objects.get(user=current_user)
		skills = user_profile.skills.all()
		total_skills = len(skills)
		midpoint = total_skills // 2  +1 # Calculate the midpoint
		skills_column1 = skills[:midpoint]  # First half of skills
		skills_column2 = skills[midpoint:]  # Second half of skills
	except Profile.DoesNotExist:
		user_profile = None
		skills_column1 = []
		skills_column2 = []

	context = {
	'user_profile': user_profile,
	'skills_column1': skills_column1,
	'skills_column2': skills_column2,
	}

	return render(request, 'portfolio/index.html', context)
	

def posts(request):
	posts = Post.objects.filter(active=True)
	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs

	page = request.GET.get('page')
	paginator = Paginator(posts, 5)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts':posts, 'myFilter':myFilter}
	return render(request, 'portfolio/posts.html', context)
	## return HttpResponse('<h1>posts</h1>')




# def posts(request):
#     # BTW you do not need .all() after a .filter() 
#     # local_url.objects.filter(global_url__id=1) will do
# 	posts = Post.objects.filter(active=True)
# 	posts =filters.PostFilter(request.GET, queryset=Post.objects.filter(active=True)).qs
# 	paginator = Paginator(posts, 5)
# 	page = request.GET.get('page')
# 	try:
# 		posts = paginator.page(page)
# 	except PageNotAnInteger:
# 		posts = paginator.page(1)
# 	except EmptyPage:
# 		posts = paginator.page(paginator.num_pages)
# 	return render(request, 'portfolio/posts.html', {'posts':posts})




def post(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		PostComment.objects.create(
			author=request.user.profile,
			post=post,
			body=request.POST['comment']
			)
		messages.success(request, "You're comment was successfuly posted!")

		return redirect('post', slug=post.slug)


	context = {'post':post}
	return render(request, 'portfolio/post.html', context)
	# return HttpResponse('<h1>post    11111</h1>')


#CRUD VIEWS
@admin_only
@login_required(login_url="home")
def createPost(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('post')

	context = {'form':form}
	return render(request, 'portfolio/post_form.html', context)


@admin_only
@login_required(login_url="home")
def updatePost(request, slug):
	post = Post.objects.get(slug=slug)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('post')

	context = {'form':form}
	return render(request, 'portfolio/post_form.html', context)

@admin_only
@login_required(login_url="home")
def deletePost(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('post')
	context = {'item':post}
	return render(request, 'portfolio/delete.html', context)



def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('portfolio/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['coderpapaa@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'portfolio/email_sent.html')

# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')

# 	if request.method == 'POST':
# 		email = request.POST.get('email')
# 		password =request.POST.get('password')

# 		#Little Hack to work around re-building the usermodel
# 		try:
# 			user = User.objects.get(email=email)
# 			user = authenticate(request, username=user.username, password=password)
# 		except:
# 			messages.error(request, 'User with this email does not exists')
# 			return redirect('login')
			
# 		if user is not None:
# 			login(request, user)
# 			return redirect('home')
# 		else:
# 			messages.error(request, 'Email OR password is incorrect')

# 	context = {}
# 	return render(request, 'portfolio/login.html', context)

# def registerPage(request):
# 	form = CustomUserCreationForm()
# 	if request.method == 'POST':
# 		form = CustomUserCreationForm(request.POST)
# 		if form.is_valid():
# 			user = form.save(commit=False)
# 			user.save()
# 			messages.success(request, 'Account successfuly created!')

# 			user = authenticate(request, username=user.username, password=request.POST['password1'])

# 			if user is not None:
# 				login(request, user)

# 			next_url = request.GET.get('next')
# 			if next_url == '' or next_url == None:
# 				next_url = 'home'
# 			return redirect(next_url)
# 		else:
# 			messages.error(request, 'An error has occured with registration')
# 	context = {'form':form}
# 	return render(request, 'portfolio/register.html', context)

# def logoutUser(request):
# 	logout(request)
# 	return redirect('home')

@login_required(login_url="home")
def userAccount(request):
	try:
		profile = Profile.objects.get(user=request.user)
	except Profile.DoesNotExist:
		profile = None

	context = {'profile':profile}
	return render(request, 'portfolio/account.html', context)
	# return HttpResponse('<h1>profile</h1>')

def profile(request):
	# return render(request, 'portfolio/profile.html')
	return HttpResponse('<h1>profile</h1>')


@login_required(login_url="home")
def updateProfile(request):
	user=request.user
	try:
		profile = Profile.objects.get(user=user)
	except Profile.DoesNotExist:
		profile = None
	context = {'profile':profile}
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('account')


	context = {'form':form}
	return render(request, 'portfolio/profile_form.html', context)