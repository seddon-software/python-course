import os, sys

# remove previous docs
os.system("rm -rf docs")

# automatically generate Sphinx sources
bin = os.path.dirname(sys.executable)
options = "-A 'Chris Seddon' -H 'Modules A to D' -F"
os.system(bin + "/sphinx-apidoc " + options + " -o docs mylib")

# build html documentation
os.chdir("docs")
os.putenv('PATH', bin + ':/usr/bin:/bin')
os.putenv('PYTHONPATH', '../mylib')
os.system('make html')

# display docs in browser
import webbrowser
try: 
    url = "file:///" + os.getcwd().replace("\\", '/') + "/_build/html/index.html"
    webbrowser.open_new_tab(url)    
except Exception as e:
    print(e)

