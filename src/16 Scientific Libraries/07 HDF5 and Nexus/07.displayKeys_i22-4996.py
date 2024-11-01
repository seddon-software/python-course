import os; os.system("clear")
'''
In this example we extract attributes from a Diamond Nexus file.  Note you can use the Dawn app to see the same information.
'''

import os
import h5py

f = h5py.File("data/i22-4996.nxs", "r")

for group in f:
    print(f[f"/{group}"])
    for subgroup in f[group]:
        print(f[f"/{group}/{subgroup}"])

import subprocess
try:
    subprocess.run("module load dawn; dawn")
except:
    print("you must be on a Diamond machine to run 'dawn'")