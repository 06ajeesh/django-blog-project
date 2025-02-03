from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django import views
from writter.models import Post
from reader.forms import CommentForm, UpdateForm
from reader.models import Comment
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

class ReaderHome(views.View):
	def get(self, request):
		user = request.user
		blogs = Post.objects.all()
		return render(request, 'reader/index.html', {'blogs': blogs})


class DetailBlog(views.View):
	def get(self, request, *args, **kwargs):
		blog_id = kwargs.get('id')
		blog = Post.objects.get(id=blog_id)
		comments = Comment.objects.filter(post=blog)
		form = CommentForm()
		return render(request, 'reader/detail_blog.html', {'blog': blog, 'form': form, "comments": comments})

	def post(self, request, *args, **kwargs):
		res = CommentForm(request.POST)
		blog_id = kwargs.get('id')
		if res.is_valid():
			comment = Comment.objects.create(
				post=Post.objects.get(id=blog_id),
				author=request.user,
				content=res.cleaned_data.get('content')
			)
			print(comment, "created successfully")
			messages.success(request, "Comment created successfully")
			return redirect("detail_blog", id=blog_id)


class SettingsView(views.View):
	def get(self, request):
		user = User.objects.get(username=request.user)
		form = UpdateForm(instance=user)
		return render(request, 'reader/settings_page.html', {'form': form})

	def post(self, request, *args, **kwargs):
		user = User.objects.get(username=request.user)
		if 'update_account' in request.POST:
			print('updating')
			res = UpdateForm(request.POST)
			if res.is_valid():
				try:
					first = res.cleaned_data.get('first_name')
					last = res.cleaned_data.get('last_name')
					email = res.cleaned_data.get('email')
					password = res.cleaned_data.get('password')
					if first:
						user.first_name = first
					if last:
						user.last_name = last
					if email:
						user.email = email
					if password:
						user.password = password
					try:
						user.save()
						print('updated')
						messages.success(request, "User updated successfully")
					except Exception as e:
						print(e)
						messages.warning(request, "User updating failed")
				except Exception as e:
					print('Error occurred', e)
					messages.error(request, "Error occurred")
			return redirect('reader_settings')

		if 'delete_user' in request.POST:
			print('deleting')
			res = user.delete()
			print(res)
			messages.warning(request, "User deleted successfully")
			return redirect('welcome')

		return HttpResponse('Error occurred')