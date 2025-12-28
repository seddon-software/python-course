from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('memory.html/', include('basic_app.urls')),
]
