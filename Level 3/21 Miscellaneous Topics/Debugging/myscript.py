#! /bin/python

# to debug this script on the command line:
# run:
#    python -m pdb myscript.py

def f(x):
    y = x * x
    print(y)


for i in range(5):
    f(i)

 