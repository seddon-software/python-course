from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('models_and_views/', include('models_and_views.urls')),
]
