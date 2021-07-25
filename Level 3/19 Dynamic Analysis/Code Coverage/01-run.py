import os
import webbrowser

def reportInBrowser():
    filename = 'htmlcov/index.html'
    from urllib.request import pathname2url
    url = f"file://{pathname2url(os.path.abspath(filename))}"
    print(url)
    webbrowser.open_new(url)

os.system("coverage run --branch code_to_be_analyzed_1.py")
os.system("coverage run -a --branch code_to_be_analyzed_2.py")
os.system("coverage annotate")  # create ,cover files
os.system("coverage html")      # create web page
reportInBrowser()

