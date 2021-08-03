import os,shutil


os.chdir("../src")
try: shutil.rmtree("dist")
except: pass

os.chdir("../src")
try: os.remove("MANIFEST")
except: pass

os.chdir("../server/repo")
try: os.remove("mymodule-1.0.zip")
except: pass


