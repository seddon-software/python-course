import sys

print("Command line parameters")

print(__file__)
# simple approach to accessing command line arguments
for i, arg in enumerate(sys.argv):
    print(f"{i}: {arg}")
print()

