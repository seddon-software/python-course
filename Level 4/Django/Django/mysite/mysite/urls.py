from django.contrib import admin
from django.urls import include, include, include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('polls/', include('polls.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
