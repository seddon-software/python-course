import json

# start with complex JSON object 
obj = '''
{
 "accounting" : [
                  { 
                    "firstName" : "John",
                    "lastName"  : "Doe",
                    "age"       : 23 
                  },
                  {
                    "firstName" : "Mary",
                    "lastName"  : "Smith",
                    "age"       : 32 
                  }
                ],
 "sales"      : [
                  {
                    "firstName" : "Sally",
                    "lastName"  : "Green",
                    "age"       : 27 
                  },
                  { 
                    "firstName" : "Jim",
                    "lastName"  : "Galley",
                    "age"       : 41 
                  }
                ]
}'''

# convert to Python
x = json.loads(obj)
print(type(x), x)

# convert back to JSON
s = json.dumps(x)
print("complex JSON object:", s)


