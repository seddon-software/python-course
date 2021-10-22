############################################################
#
#    Using with
#
############################################################

# successful read
try:
    with open("data/hello.txt", "r") as f:
        for line in f:
            print(line, end="")
except IOError as e:
    print(e)

# unsuccessful read
try:
    with open("data/unknown-file.txt", "r") as f:
        for line in f:
            print(line, end="")
except IOError as e:
    print(e)


