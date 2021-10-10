import os

def createHugeFile():
    os.system("echo 'This is a line of text' > huge_file_1")
    for n in range(1, 30):
        os.system(f"cat huge_file_{n} huge_file_{n} >> huge_file_{n+1}") 
        os.system(f"rm huge_file_{n}")     
        os.system(f"ls -lh huge_file_{n+1}") 

def cleanup():
    os.system("rm huge_file_30")
    
# python won't allow you to read a file into memory if it is > 4GB in size
# so this fails:
def readFileInOneGo():
    try:
        f = open("huge_file_30", "r")
        contents = f.read()
    except Exception as e:
        print("can't read file into memory", e)

# use an infinite generator to read the file (this works)
# and compute the size of the file
def useInfiniteIteratorToReadFile():
    f = open("huge_file_30", "r")
    n = 0
    for line in f:
        n += len(line)
    
    print(f"size = {n}")


def main():
    createHugeFile()
    print("Attempting to read file in one go")
    readFileInOneGo()
    print("Attempting to read file using an infinite generator")
    useInfiniteIteratorToReadFile()
    cleanup()

main()
