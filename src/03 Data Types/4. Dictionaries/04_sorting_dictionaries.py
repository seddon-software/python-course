############################################################
#
#    dictionary
#
############################################################

# Dictionaries do not define an order.  However since Python 3.7
# dictionary have a backing array which contains keys in the order in
# which entries were added to the dictionary.

# If you want to print a dictionary in lexical order of the keys
# you need to use a sorted list containing the keys
 

# set up a dictionary
salary = {
          "john":  34000, 
          "sara":  27000,
          "pedro": 52000,
          "tim":   12500,
          "zoe":   66000
         }

# extract the keys and sort them
mylist = list(salary.keys())
mylist.sort()

# go back to the hash and pick up the values
for key in mylist:
    print(f"{key:>6s}{salary[key]:6}")
    


