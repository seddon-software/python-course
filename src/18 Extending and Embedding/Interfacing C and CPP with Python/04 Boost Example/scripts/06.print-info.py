import sys
from distutils.sysconfig import get_python_lib


def displayInfo(baseFileName):
    version = str(sys.version[0:3])
    eggInfoFile = get_python_lib() + "/" + baseFileName + version + ".egg-info"
    try:
        f = open(eggInfoFile, 'r')
        print(f.read())
    except:
        pass

displayInfo("GreetingPackage-1.0-py")

