import os
import webbrowser
from urllib.request import pathname2url

def reportInBrowser():
    os.system("coverage html")      # create web page
    filename = 'htmlcov/index.html'
    url = f"file://{pathname2url(os.path.abspath(filename))}"
    print(url)
    webbrowser.open_new(url)

if __name__ == "__main__":
    reportInBrowser()


