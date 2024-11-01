'''
The latest Unicode standard is 14.0.0 (10 September 2024):
            https://www.unicode.org/versions/Unicode16.0.0/

This defines 154,998 different characters, encompassing alphabets for many languages and various symbols.  Each 
character is assigned a unique number or code point although this number is not necessarily the one used in 
programs.  Instead various encodings are used, such as UTF-8, UTF-16 and UCS-2. 

THe "chr()" function is used to work directly with code points.  Here we display "Unicode Box Drawing" and 
"Arabic" code points by way of example.
'''

def printRange(title, lo, hi):
    print(f"{title}: {lo:04x}H-{hi:04x}H")
    for n in range(lo, hi+1):
        print(chr(n), end="")
    print()

print()
printRange("Unicode Box Drawing", 0x2500, 0x257F)
print()
printRange("Arabic", 0x0600, 0x06FF)
print()
