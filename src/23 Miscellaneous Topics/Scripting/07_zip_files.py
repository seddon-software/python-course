############################################################
#
#    zip files
#
############################################################

import os
os.chdir("zipfiles")


import zipfile
zipfile.ZipFile("src.zip", "r").extractall()


import shutil
shutil.rmtree("src")
