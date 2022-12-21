'''
Here we use the coverage module to check how well our unit tests are working.  The module tests are working
with the file:
            src/mycode.py
            
which defines a function called:
            def process_input(a, b, operation):

Each successive test covers more and more parts of his function.  Results are presented in web page tabs.
'''

import os, webbrowser
from pathlib import Path

def displayInBrowser(attempt):
    os.chdir("tests")
    os.system(f"coverage run --branch -m unittest {attempt}.py")
    os.system(f"coverage html -d {attempt} --title={attempt}")      # create web page
    url = f"{Path(os.getcwd())}/{attempt}/index.html"
    webbrowser.open_new_tab(url)
    os.chdir("..")

if __name__ == "__main__":
    displayInBrowser("test_part1")
    displayInBrowser("test_part2")
    displayInBrowser("test_part3")
    displayInBrowser("test_part4")

