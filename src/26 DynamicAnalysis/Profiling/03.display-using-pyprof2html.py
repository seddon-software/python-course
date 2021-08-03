import pyprof2html

# run profiling.py first
# this creates files in the stats directory

converter = pyprof2html.Converter("stats/profilestats.out")
converter._hookhtml()

# display html/index.html in web browser
import webbrowser, os
url = os.getcwd().replace('\\', '/')  # getcwd() returns slashes the wrong way round for a browser
url = "file:///" + url + "/html/index.html"
print(url)
webbrowser.open_new(url)

1
