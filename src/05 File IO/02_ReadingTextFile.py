############################################################
#
#    Reading a file
#
############################################################

# successful read
try: 
    f = open("data/hello.txt", "r")
    try:
        for line in f:
            print(line, end=" ")
    finally:
        f.close()
except IOError as e:
    print(e)


# unsuccessful read
try: 
    f = open("./data/unknown-file.txt", "r")
    try:
        for line in f:
            print(line, end=" ")
    finally:
        f.close()
except IOError as e:
    print(e)

