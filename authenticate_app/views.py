from django.shortcuts import render, redirect
from django import views
from django.views.generic import TemplateView
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


class WelcomeView(TemplateView):
	template_name = 'welcome_page.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['logform'] = LoginForm()
		context['regform'] = RegisterForm()
		return context

	def post(self, request, *args, **kwargs):
		if 'login_form' in request.POST:
			print('login')
			username = request.POST.get("username")
			password = request.POST.get("password")
			login_as = request.POST.get("login_as")
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				messages.success(request, "Login Successfully")
				print('-------------------')
				print('Successfully login')
				print("value of superuser is: ", login_as)
				if login_as == "writer":
					return redirect('creator_home')
				elif login_as == "viewer":
					return redirect('viewer_home')
			else:
				messages.warning(request, "Invalid credentials")
				return redirect('welcome')

		if 'register_form' in request.POST:
			print('register')
			print(request.POST)
			res = RegisterForm(request.POST)
			# print(res)
			if res.is_valid():
				try:
					User.objects.create_user(**res.cleaned_data)
					messages.success(request, "User created successfully")
				except Exception as e:
					messages.error(request, f"Error {e} Occurred during Creating User")
				return redirect('welcome')
			else:
				messages.error(request, "Error Occurred during Creating User")
				return redirect('welcome')

		else:
			print('Error')
			messages.error(request, "Error Occurred")
			return redirect('welcome')


# class LoginView(views.View):
# 	def get(self, request):
# 		return render(request, "login_form.html", {"form": LoginForm()})
#
# 	def post(self, request, *args, **kwargs):
# 		username = request.POST.get("username")
# 		password = request.POST.get("password")
# 		login_as = request.POST.get("login_as")
# 		user = authenticate(request, username=username, password=password)
# 		if user:
# 			login(request, user)
# 			messages.success(request, "Login Successfully")
# 			print('-------------------')
# 			print('Successfully login')
# 			print("value of superuser is: ", login_as)
# 			if login_as == "writer":
# 				return redirect('creator_home')
# 			elif login_as == "viewer":
# 				return redirect('viewer_home')
# 		else:
# 			messages.warning(request, "Invalid credentials")
# 			return redirect('login_form')


# class RegisterFormView(views.View):
# 	def get(self, request):
# 		return render(request, "register_form.html", {"form": RegisterForm()})
#
# 	def post(self, request):
# 		print(request.POST)
# 		res = RegisterForm(request.POST)
# 		if res.is_valid():
# 			# res.save()
# 			f_name = res.cleaned_data.get('first_name')
# 			l_name = res.cleaned_data.get('last_name')
# 			u_name = res.cleaned_data.get('username')
# 			email = res.cleaned_data.get('email')
# 			password = res.cleaned_data.get('password')
# 			User.objects.create_user(first_name=f_name, last_name=l_name, username=u_name, email=email,
# 									 password=password)
# 			messages.success(request, "User created successfully")
# 			return redirect('login_form')
# 		else:
# 			return HttpResponse("<center>Error Occurred during Sending</center>")


class LogoutView(views.View):
	def get(self, request):
		logout(request)
		messages.info(request, "User Logout successfully")
		return redirect('welcome')