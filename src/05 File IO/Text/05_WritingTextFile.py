############################################################
#
#    Writing to a file
#
############################################################

def writeFileContents(filename, data):
    try: 
        # w (write) will empty an existing file before opening it
        f = open(filename, "w")
        f.writelines(data)
    except IOError as e:
        print(e)
    finally:
        try: 
            f.close()
        except: 
            pass    # can't do anything if close throws

FILENAME = "data/text.txt"
data = ("line 1\n", "line 2\n", "line 3\n", "line 4\n", "line 5\n")
writeFileContents(FILENAME, data)

import os
os.system(f"cat {FILENAME}")


