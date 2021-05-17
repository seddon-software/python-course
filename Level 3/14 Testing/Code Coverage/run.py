import os
import webbrowser

os.environ["PATH"] = "/Users/seddon/Anaconda3/anaconda/bin/:" + os.environ["PATH"]
os.system("coverage run --branch code_to_be_analyzed_1.py")
os.system("coverage annotate")
os.system("/bin/cat code_to_be_analyzed_2.py,cover")
os.system("coverage html")

filename = 'htmlcov/index.html'
from urllib.request import pathname2url
url = 'file://{}'.format(pathname2url(os.path.abspath(filename)))
print(url)
webbrowser.open_new(url)
