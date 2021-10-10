import tarfile, os, subprocess,glob

# It's worth mentioning that you can get better compression when you tar and then compress than if you were to compress each file individually
fileName = "out/MyFile.tar.gz"

tar = tarfile.open(fileName, "w:gz")
inFiles = glob.glob("*.py")

for f in inFiles:
    tar.add(f)
tar.close()

cmd = "tar tvf {0}".format(fileName)
subprocess.call(cmd.split())
