from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('basic_app/', include('basic_app.urls')),
]
