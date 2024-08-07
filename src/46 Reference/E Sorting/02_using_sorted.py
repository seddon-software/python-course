'''
More on Sorted
==============

Here is a further example.  This time we use various key functions including a lambda.
'''

data = [ [ 5, ('G', 29.5), "Monday",    "file17.py", 70],
         [11, ('B', 32.9), "Wednesday", "file51.py", 45],
         [15, ('F',  6.7), "Saturday",  "file76.py", 32],
         [ 7, ('D',  8.6), "Sunday",    "file34.py", 97],
         [ 8, ('E', 21.3), "Tuesday",   "file23.py", 56],
         [ 5, ('C', 52.5), "Friday",    "file11.py", 28],
         [20, ('A', 24.4), "Thursday",  "file19.py", 29],
        ]

def keyFunction(row):
    return row[1][1]

print("key function returns element [1][1]; this is the second part of the tuple")
sortedData = sorted(data, key=keyFunction, reverse=True)
for d in sortedData: 
    print(d)
print()

print("key function is a lambda returning element [3]; this is the fileName")
sortedData = sorted(data, key=lambda row:row[3], reverse=True)
for d in sortedData: print(d)
print()

print("key function is a lambda returning [1][0]; this is the first part of the tuple")
sortedData = sorted(data, key=lambda row:row[1][0], reverse=False)
for d in sortedData: print(d)
print()
