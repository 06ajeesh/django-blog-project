from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	images = models.ImageField(upload_to='uploads/images/', blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	slug = models.SlugField(unique=True, blank=True)
	status = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		if not self.slug:  # If no slug is provided
			self.slug = slugify(self.title)
		if self.slug:
			self.slug = slugify(self.slug)
		# Else, leave the user-provided slug as is.
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title