############################################################
#
#    Writing to a file
#
############################################################

import os; os.system("clear")

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

data = ("line 1\n", "line 2\n", "line 3\n", "line 4\n", "line 5\n")
writeFileContents("data/text.txt", data)


