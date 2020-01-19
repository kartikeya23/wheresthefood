from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Categories, Customer, Item, Table
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home(request):
	return render(request, 'restaurant/home.html')


def signup(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		# User has info and wants an account now
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				auth.login(request, user)
				return redirect('home')
		else:
			return render(request, 'restaurant/signup.html', {'error': 'Passwords dont match'})
	else:
		# User wants to enter info
		return render(request, 'restaurant/signup.html')


def login(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == "POST":
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			print("User logged in:", user.username)
			return redirect('home')
		else:
			print('Unknown User')
			return render(request, 'restaurant/login.html', {'error': 'user not found'})
	else:
		return render(request, 'restaurant/login.html')


def logout(request):
	if request.method == 'POST':
		auth.logout(request,)
		return redirect('login')


@login_required(login_url='/login')
def book(request):
	order = request.user.customer.order
	return render(request, 'restaurant/cart.html', {'items': order})

