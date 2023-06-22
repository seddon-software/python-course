'''
Dictionaries (dict) are one of the most important data structures in Python.  Each entry in a dict
comprises of a key-value pair.  The key is usually a string and must be unique and immutable.  The value
can be anything.

To initialize a dict called salary we write code of the form:
            salary = {key:value, key:value, key:value ...}

but to update an entry we write:
            salary[key] = newValue

'''


# dict      key  : value
salary = {"Susan": 33000, 
          "John" : 27000,
          "Zak"  : 27000,
          "Jim"  : 24000,
          "Zoe"  : 29000}

# key must be unique and immutable
# value doesn't have to be unique

# update an entry at run-time (using existing key)
salary["Zak"] = salary["Zak"] * 1.1

# introduce a new key (creates a new key-value pair)
salary["Chris"] = 50000

# extract key-value pairs with item()
for key, value in salary.items():
    print(f"{key}'s salary is {value:,.2f}") # format with 2 decimal places and commas after thousands

# extract values with values() and calculate average salary
listOfSalaries = list(salary.values())
averageSalary = sum(listOfSalaries) / len(listOfSalaries)
print(f"Average salary is {averageSalary:,.2f}")
