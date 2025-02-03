from django.urls import path
from writter.views import WriterHome,BlogUpdateView,SettingsView,BlogDelete

urlpatterns = [
	path('', WriterHome.as_view(), name='creator_home'),
	path('update/<int:id>', BlogUpdateView.as_view(), name='update_blog'),
	path('delete/<int:id>', BlogDelete.as_view(), name='delete_blog'),
	path('settings', SettingsView.as_view(), name='writer_settings'),
]