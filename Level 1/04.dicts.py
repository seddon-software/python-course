'''
Dictionaries (dict) are one of the most important data structures in Python.  Each entry in a dict
comprises of a key-value pair.  The key is usually a string and must be unique and immutable.  The value
can be anything.

To initialize a dict called salary we write code of the form:
            salary = {key:value, key:value, key:value ...}

but to update an entry we write:
            salary[key] = newValue

'''

salary = {
          'jim'  : 30000,
          'sue'  : 28000,
          'peter': 41000,
          'zoe'  : 51000,
          'kwazi': 500000
         }


salary['peter'] = 22222
salary['george'] = 22222
print(salary)

name = 'peter'
print(f"{name}'s salary is {salary[name]}")
