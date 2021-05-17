fileName = "data/myfile-1.bin"

try:
    with open(fileName, "rb") as f:
        x = f.read()
        print(type(x), x) 
        print(list(x))
except IOError as e:
    print(e)
    