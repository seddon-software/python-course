import re


filename = "data/customer.txt"
f = open(filename, "r")

data = f.readlines()
customer = dict();

keyCols = ('firstName', 'initial', 'lastName')    
valueCols = ('empNo', 'dept', 'phone', 'hiredate', 'job', 'sex', 'birthDate', 'salary', 'bonus', 'commission')
print("key cols: {keyCols}")
print("value cols: {valueCols}")

for line in data:
    fields = line.split(";", 2)

    # ignore blank lines and those without a semicolon
    if len(fields)!= 2: continue
    
    # fields[0] contains EmpNo and the Key
    # fields[1] contain the other fields, but starts with whitespace
    pattern = re.compile(r"[\s]+")    
    part1 = pattern.split(fields[0])
    part2 = pattern.split(fields[1].strip())
    
    # part1 will have 3 or 4 items depending on whether or not there is a middle initial 
    if len(part1) == 3:
        empNo, firstName, lastName = part1
        initial = ""
    else:
        empNo, firstName, initial, lastName = part1

    # now pack the fields into the hash = {key, value}
    key = (firstName, initial, lastName)
    value = [empNo]
    value.extend(part2)
    customer[key] = value

# search for two different entries
key = ('WILLIAM', 'T', 'JONES')
print(key, customer[key])

key = ('DAVID', '', 'BROWN')
print(key, customer[key])
