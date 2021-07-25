############################################################
#
#    functors
#
############################################################

# test data
salary = {
          "John"  : 47000,
          "Mary"  : 24000,
          "Zoe"   : 17000,
          "Carla" : 34000,
          "Pedro" : 25000,
          }

# library code simulating findIf C++ algorithm
def findIf(hash, predicate):
    for key, value in hash.items():
        if predicate(value): break
    else:
        return None
    return key, value


# 3 ways of using this algorithm
# method 1: use a function for each case
def lessThan21K(param):
    if param < 21000:
        return True
    else:
        return False

def lessThan25K(param):
    if param < 25000:
        return True
    else:
        return False

print(findIf(salary, lessThan21K))
print(findIf(salary, lessThan25K))

# method 2: use a Functor
class Functor:
    def __call__(self, param):
        if param < self.salary:
            return True
        else:
            return False
        
    def __init__(self, s):
        self.salary = s
        
print(findIf(salary, Functor(21000)))
print(findIf(salary, Functor(25000)))


# method 3: add attribute to funtion
def lessThan(param):
    if param < lessThan.salary: # uses attribute of function
        return True
    else:
        return False

lessThan.salary = 21000
print(findIf(salary, lessThan))
lessThan.salary = 25000
print(findIf(salary, lessThan))



    

1