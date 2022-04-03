import subprocess,os,sys
sys.path.append('../..')
import set_paths


os.chdir("../src")
response = subprocess.run("ls *.egg-info/PKG-INFO", shell=True, capture_output=True)
eggFile = response.stdout.decode()
subprocess.call(f"cat {eggFile}".split())

# installedFiles = open("files.txt", "r")
# for file in installedFiles:
#     file = file.rstrip()
#     if file.endswith("egg-info"):
#         try:
#             f = open(file, 'r')
#             print(f.read())
#         except:
#             pass
        
