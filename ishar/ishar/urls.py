from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from rest_framework.urlpatterns import format_suffix_patterns
from isharonline import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('isharonline.urls')),
    url(r'^meditations/', views.MeditationList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
