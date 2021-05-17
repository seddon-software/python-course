import os, sys
from distutils.sysconfig import get_python_lib, get_config_vars

os.chdir(get_python_lib())
version = sys.version[0:3]
eggInfo = "GreetingPackage-1.0-py" + version + ".egg-info"
shared_object = "greeting" + get_config_vars("SO")[0]

try: os.remove(eggInfo)
except Exception as e: print(e)

try: os.remove(shared_object)
except Exception as e: print(e)


print("Example uninstalled")


