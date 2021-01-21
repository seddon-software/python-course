import json

# start with Python list
mylist = [1, '2', 3, "4", 5]
print(type(mylist), mylist)

#convert to JSON string
s = json.dumps(mylist)
print("JSON", type(s), s)

# convert back to Python list
newList = json.loads(s)
print(type(newList), newList)
