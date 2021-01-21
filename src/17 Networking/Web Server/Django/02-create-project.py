import sys, os
from single_step import s

def windows():
    s('deltree src')
    s('md src')

def unix():
    s('rm -rf src')
    s('mkdir src')


if sys.platform == "win32":
    windows()
else:
    unix()

s('cd src')
s('django-admin startproject mysite')
