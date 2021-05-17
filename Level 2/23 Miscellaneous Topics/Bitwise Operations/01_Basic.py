x = 0x53FE13
y = 0xFF00FF

print("{0:08x}".format(x & y))   # bitwise and
print("{0:08x}".format(x | y))   # bitwise or
print("{0:08X}".format(~x))      # 1's complement
print("{0:08X}".format(x ^ y))   # exclusive or
print("{0:08X}".format(x >> 4))  # shift right
print("{0:08X}".format(x << 4))  # shift left

# work with 1031
print(0x0407)                    # hex to decimal
print(hex(1031))                 # decimal to hex
print(bin(1024 + 7))             # decimal to binary
print(int('0b10000000111', 2))   # binary to decimal



