'''
The latest Unicode standard is 17.0.0 (9 September 2025):
            https://www.unicode.org/versions/Unicode17.0.0/
            

This defines 159,801  different characters, encompassing alphabets for many languages and various symbols.  Each 
character is assigned a unique number or code point although this number is not necessarily the one used in 
programs.  Instead various encodings are used, such as UTF-8, UTF-16 and UCS-2. 

The "chr()" function is used to work directly with code points.  Here we display "Unicode Box Drawing" and 
"Arabic" code points by way of example.

In this example we also print out the ASCII (American Standard Code for Information Interchange) characters in range 32-126.
The ASCII standard is also an ISO standard. 
'''


def printRange(title, lo, hi):
    # using chr()
    print(f"{title}: {lo:04x}H-{hi:04x}H")
    for n in range(lo, hi+1):
        print(chr(n), end="")
    print()
    # using formatted output
    for n in range(lo, hi+1):
        print(f"{n:c}", end="")
    print()

print()
printRange("Unicode Box Drawing", 0x2500, 0x257F)
print()
printRange("Arabic", 0x0600, 0x06FF)
print()
printRange("printable ASCII", 32, 127)
print()
