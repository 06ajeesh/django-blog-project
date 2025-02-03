from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', "last_name", "username", "email", "password"]
		widgets = {
			'first_name': forms.TextInput(
				attrs={"class": "form-control", "placeholder": "first_name", "id": "id_first_name", "required": "required"}),
			'last_name': forms.TextInput(
				attrs={"class": "form-control", "placeholder": "last_name", "id": "id_last_name", "required": "required"}),
			'username': forms.TextInput(
				attrs={"class": "form-control", "placeholder": "username", "id": "id_username", "required": "required"}),
			'email': forms.EmailInput(attrs={"class": "form-control", "placeholder": "email", "id": "id_email",	"required": "required"}),
			'password': forms.PasswordInput(
				attrs={"class": "form-control", "placeholder": "password", "id": "id_password",	"required": "required"}),
		}


class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']
		widgets = {
			'username': forms.TextInput(
				attrs={"class": "form-control", "placeholder": "username", "id": "id_username"}),
			'password': forms.PasswordInput(
				attrs={"class": "form-control", "placeholder": "password", "id": "id_password"}),
		}