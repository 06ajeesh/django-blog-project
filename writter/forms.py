from django import forms
from django.contrib.auth.models import User
from writter.models import Post


class BlogForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'images', 'slug']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Title", "id": "id_title"}),
			'content': forms.Textarea(
				attrs={'class': 'form-control h-auto', 'placeholder': "Content", "id": "id_content"}),
			'images': forms.FileInput(attrs={
				'class': 'form-control', 'placeholder': "images", "id": "id_image"
			}),
			'slug': forms.TextInput(
				attrs={'class': 'form-control', 'placeholder': "slug", "id": "id_slug", 'maxlength': '50'}),
		}
		labels = {
			'title': "Title",
			'content': "Contents",
			'images': 'Image',
			'slug': "Slug (-Optional-)",
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