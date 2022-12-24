'''
Objects normally store their attributes in dicts.  However slots were introduced as an alternative, supposedly
for performance reasons.  Here we compare slots based objects with convential objects and for good measure we 
see how this compares with using a dict directly.

Bypassing the class mechanism is certainly faster, but the coding is clearly more complex.  So although we
do get a speed up, code clarity is always more important.'''

from timeit import timeit

count = 1000 * 1000

print("\n*** Creating instances ***")
print("class", timeit("p = Person('Susan',25,'London')", "from myprogram import Person", number = count))
print("slots", timeit("p = PersonSlots('Susan',25,'London')", "from myprogram import PersonSlots", number = count))
print("dict ", timeit("p = {'name' : 'Susan', 'age' : 25, 'address' : 'London' }", number = count))
        

print("\n*** Calling methods ***")
print("class", timeit("s = p.getDetails()",
                      "from myprogram import Person;" +
                      "p = Person('Susan',25,'London')", number = count))
print("slots", timeit("s = p.getDetails()",
                      "from myprogram import PersonSlots;" +
                      "p = PersonSlots('Susan',25,'London')", number = count))
print("dict ", timeit("s = p['name'] + ',' + str(p['age']) + ',' + p['address']", 
                     "p = {'name' : 'Susan', 'age' : 25, 'address' : 'London' }", number = count))


1
