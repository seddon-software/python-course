'''
Use the h5dump command on the command line to inspect a Nexus file
'''

import os
NexusFile = "data/MoKedge_1_15.nxs"

# get help
os.system("h5dump --help")
input("Continue?")

# get a full dump of Nexus file
os.system(f"h5dump {NexusFile}")
input("Continue?")

# list groups and datasets
os.system(f"h5dump --contents {NexusFile}")
input("Continue?")

# just look at one attribute
os.system(f"h5dump --attribute file_name {NexusFile}")
input("Continue?")

# look at one group
os.system(f"h5dump --group /entry1/counterTimer01 {NexusFile}")
input("Continue?")

