'''
inspect_whl._file
=================
A ".whl" file is just a zip file with a different extension.
'''

import subprocess, os
import pprint
from zipfile import ZipFile

os.chdir("../src/dist")
response = subprocess.run("ls *.whl", shell=True, capture_output=True)
wheelFile = response.stdout.decode().strip()

zip = ZipFile(wheelFile).namelist()
pprint.pprint(zip)

