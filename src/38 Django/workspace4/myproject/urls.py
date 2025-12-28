from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('models_app/', include('models_app.urls')),
]
