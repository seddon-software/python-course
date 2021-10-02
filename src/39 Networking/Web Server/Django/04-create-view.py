import sys, os
from single_step import s

s('cd src/mysite/polls')
code = r"""
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
"""

s('cat <<XXX >views.py ' + code + '\nXXX' )
