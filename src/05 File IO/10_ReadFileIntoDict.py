

def getFileContents(filename):
    try: 
        with open(filename, "r") as f:
            allLines = f.readlines()
        return allLines
    except IOError as e:
        print(e)


salary = {}
lines = getFileContents("data/salaries.txt")

for line in lines:
    key, value = line.split(',')
    key = key.strip()
    value = value.strip()
    salary[key] = value

print("perform a lookup on Zoe")
print("=======================")
print(("Zoe : ", salary["Zoe"]))
print()


print("print dictionary in lexical order")
print("=================================")
keys = list(salary.keys())
keys.sort()

# print out salaries in lexical order
for key in keys:
    print((key, ":", salary[key]))

1

