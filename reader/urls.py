from django.urls import path
from reader.views import ReaderHome, DetailBlog, SettingsView

urlpatterns = [
	path('', ReaderHome.as_view(), name='viewer_home'),
	path('detail_blog/<int:id>', DetailBlog.as_view(), name='detail_blog'),
	path('settings', SettingsView.as_view(), name='reader_settings'),
]