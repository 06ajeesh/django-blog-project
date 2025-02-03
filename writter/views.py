from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponse
from writter.models import Post
from writter.forms import BlogForm, UpdateForm
from django.contrib import messages


# Create your views here.

class WriterHome(View):
	def get(self, request):
		blogs = Post.objects.filter(author=request.user)
		return render(request, 'writer/index.html', {'form': BlogForm(), 'blogs': blogs})

	def post(self, request, *args, **kwargs):
		res = BlogForm(request.POST, request.FILES)
		if res.is_valid():
			user = self.request.user
			post = Post.objects.create(author=user, **res.cleaned_data)
			print("post value return is : ", post)
			messages.success(request, "Success")
			return redirect('creator_home')
		else:
			messages.error(request, "Error Occured")
			return redirect('creator_home')


class BlogUpdateView(View):
	def get(self, request, *args, **kwargs):
		blog_id = kwargs.get('id')
		blog = Post.objects.get(id=blog_id)
		form = BlogForm(instance=blog)
		comments = blog.comments.all()
		return render(request, 'writer/update_blog.html', {'form': form, 'comments': comments,'blog':blog})

	def post(self, request, *args, **kwargs):
		blog_id = kwargs.get('id')
		blog = Post.objects.get(id=blog_id)
		title = request.POST.get('title')
		content = request.POST.get('content')
		images = request.FILES.get('images')
		slug = request.POST.get('slug')
		try:
			blog.title = title
			blog.content = content
			blog.images = images
			blog.slug = slug
			blog.save()
			messages.success(request, "Success")
		except Exception as e:
			print(e)  # print form errors
			print("Form data: ", request.POST)  # print sent data
			messages.error(request, "Error Occured")
		finally:
			return redirect('creator_home')


class BlogDelete(View):
	def post(self, request, *args, **kwargs):
		blog_id = kwargs.get('id')
		blog = Post.objects.get(id=blog_id)
		blog.delete()
		messages.warning(request, "Deleted Successfully")
		return redirect('creator_home')


class SettingsView(View):
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
					user.save()
					print('updated')
				except Exception as e:
					print('Error occurred', e)
			return redirect('reader_settings')

		if 'delete_user' in request.POST:
			print('deleting')
			res = user.delete()
			print(res)
			return redirect('welcome')

		return HttpResponse('Error occurred')