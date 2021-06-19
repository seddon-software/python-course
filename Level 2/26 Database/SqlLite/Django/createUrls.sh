cd mysite

cat << EOF > salaries/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
EOF

cat << EOF > mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('salaries/', include('salaries.urls')),
    path('admin/', admin.site.urls),
]
EOF
