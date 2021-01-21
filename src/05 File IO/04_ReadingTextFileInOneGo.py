############################################################
#
#    File I/O
#
############################################################

def getFileContents(filename):
    try: 
        f = open(filename, "r")
        allLines = f.readlines()
        return allLines
    except IOError as e:
        print(e)
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws

lines = getFileContents("data/hello.txt")
for line in lines:
    print("--{}".format(line), end="")
    
