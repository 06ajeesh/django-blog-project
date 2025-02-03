from django import forms
from reader.models import Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']
		widgets = {
			'content': forms.TextInput(attrs={"class": "form-control", "placeholder": "content", "id": "id_comment"}),
		}


class UpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password']
		widgets = {
			'first_name': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': 'first name', 'id': 'id_first_name'}),
			'last_name': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': 'last name', 'id': 'id_last_name'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email', 'id': 'id_email'}),
			'password': forms.PasswordInput(
				attrs={'class': 'form-control', 'placeholder': 'password', 'id': 'id_password'}),
		}

		labels = {
			'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email', 'password': 'Update Password'
		}

	password = forms.CharField(required=False, widget=forms.PasswordInput(
		attrs={'class': 'form-control', 'placeholder': 'password', 'id': 'id_password'}))