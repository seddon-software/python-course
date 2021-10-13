############################################################
#
# Print Unicode Code Points
#
############################################################

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
