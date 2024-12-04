from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('forms/', include('forms.urls')),
]
