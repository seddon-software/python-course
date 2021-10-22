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
          "rocco": 12500,
          "zoe":   66000
         }
salary["sara"] = 28000
salary["sara"] = None
salary["george"] = 137000

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

# enumerate all key value pairs
for i, (key, value) in enumerate(salary.items()):
    print(i, key, value)

# check if key in dictionary
if "george" in salary: print("george is in dictionary")
if "sara" in salary: print("sara is in dictionary")
if "tom" not in salary: print("tom is NOT in dictionary")

# delete keys using del or pop
del salary["zak"]           # nothing returned
value = salary.pop("sara")

# print whole dictionary
print(salary)  # preserves input order


