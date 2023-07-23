'''
ascii
=====
This example prints out the ASCII (American Standard Code for Information Interchange) characters in range 32-126.
The ASCII stand is also an ISO standard. 
'''

# printable characters in range 32-126
for ch in range(32, 127):
    print(f"{ch:c}", end="")
print()
