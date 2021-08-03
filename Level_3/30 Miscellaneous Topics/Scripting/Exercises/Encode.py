name = raw_input("Enter name to encode: ")

def method1():
    import string
    print name.translate(string.maketrans("abcdefghijklmnopqrstuvwxyz", 
                                          "bcdefghijklmnopqrstuvwxyza"))

def method2():                    
    # split into list
    chars = list(name)
    charList = []
    
    # encode list
    for c in chars:
        if c == "z":
            e = chr(ord(c) -25)
        else:
            e = chr(ord(c) + 1)
        charList.append(e)
    
    # convert back to string
    encodedName = "".join(charList)
    print encodedName


method1()
method2()
