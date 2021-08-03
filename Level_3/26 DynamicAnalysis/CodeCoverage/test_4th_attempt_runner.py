#!/usr/bin/env python

import os, webbrowser
from urllib.request import pathname2url

if __name__ == "__main__":
    os.system("coverage run -m unittest test_4th_attempt.py")
    os.system("coverage annotate")  # create annotated '*,cover' file
    os.system("coverage html")      # create web page
    url = f"file://{pathname2url(os.path.abspath('htmlcov/index.html'))}"
    webbrowser.open_new(url)


