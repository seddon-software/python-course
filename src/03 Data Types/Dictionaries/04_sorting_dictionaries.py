############################################################
#
#    dictionary
#
############################################################

# set up a dictionary
salary = {
          "john":  34000, 
          "sara":  27000,
          "pedro": 52000,
          "tim":   12500,
          "zoe":   66000
         }

mylist = list(salary.keys())
mylist.sort()

for key in mylist:
    print("{:>6s}{:6d}".format(key, salary[key]))
    


