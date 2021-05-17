############################################################
#
#    dictionary
#
############################################################

# set up a dictionary
salary = {
 		  "zak":   34000, 
          "sara":  27000,
          "pedro": 52000,
          "kilas": 12500,
          "zoe":   66000
         }
salary["sara"] = 28000
salary["sara"] = None
salary["george"] = 137000

# delete keys using del and pop
del salary["zak"]
value = salary.pop("kilas")

# read and write
salary["pedro"] = 53000
print(salary["pedro"])

# print all the keys
for key in salary.keys():
    print(key, end=' ')
print()

# print all the values
for value in salary.values():
    print(value, end=' ')
print()

# print all <key,value> pairs
for key, value in salary.items():
    print(key, value)

# check if key in dictionary
if "george" in salary: print("george is in dictionary")

if "sara" in salary: print("sara is in dictionary")

1
