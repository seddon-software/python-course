import sys, os
from single_step import s


code1 = r"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
"""

code2 = r"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
"""


s('cd src/mysite')
s('cat <<XXX >polls/urls.py ' + code1 + '\nXXX' )
s('cat <<XXX >mysite/urls.py ' + code2 + '\nXXX' )

