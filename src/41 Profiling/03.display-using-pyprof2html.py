'''
The pyprof2html module converts profile binary data to html.  Unfortunately the module lacks documentation.
Important methods rather unusually start with underscores, such as the method to generate html:
            _hookhtml()

You may need to install the pyprof2html module with: 
            python -m pip install pyprof2html --user
'''

import pyprof2html
from pathlib import Path

# run profiling.py first
# this creates files in the stats directory

converter = pyprof2html.Converter("stats/profilestats.out")
converter._hookhtml()

# display html/index.html in web browser
import webbrowser, os
url = f"file:///{Path(os.getcwd())}/html/index.html"
print(url)
webbrowser.open_new(url)


