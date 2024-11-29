from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tennis/', include('tennis.urls')),
    path('admin/', admin.site.urls),
]
