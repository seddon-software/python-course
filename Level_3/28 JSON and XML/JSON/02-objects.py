import json

# start with Python dict
myDict = {
         'mon' : 'Monday', 
         'tue' : 'Tuesday',
         'wed' : 'Wednesday', 
         'thu' : 'Thursday', 
         'fri' : 'Friday' }
print(type(myDict), myDict)

# convert to JSON object
obj = json.dumps(myDict)
print("JSON object:", obj)

# convert back to Python dict
newDict = json.loads(obj)
print(type(newDict), newDict)

