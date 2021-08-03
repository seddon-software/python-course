import os, subprocess
import pkgutil
import webbrowser

packageToInspect = "xlwt"
thePackage = __import__(packageToInspect)


def walkPackages(package):
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        if ispkg: 
            walkPackages(modname)
        else:
            cmd = "python -m pydoc -w {0}.{1}".format(package.__name__, modname)
            print(cmd)
            subprocess.call(cmd.split())
            

os.chdir('html')
walkPackages(thePackage)

url = "file://{0}/{1}.html".format(os.getcwd(), packageToInspect)

try:
    # Open URL in new window, raising the window if possible.
    webbrowser.open_new(url)
except Exception as e:
    print(e)
