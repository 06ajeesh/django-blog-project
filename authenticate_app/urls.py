from django.urls import path
from authenticate_app import views

urlpatterns = [
	path('', views.WelcomeView.as_view(), name='welcome'),
	# path('login', views.LoginView.as_view(), name='login_form'),
	# path('register', views.RegisterFormView.as_view(), name='register_form'),
	path('logout', views.LogoutView.as_view(), name='logout'),
]