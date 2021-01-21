from timings import Timings

Timings.titles()
t1 = Timings(title = "class", setup = "from myprogram import Person", 
                              statement = "p = Person('Susan',25,'London')")
t2 = Timings(title = "slots", setup = "from myprogram import PersonSlots", 
                              statement = "p = PersonSlots('Susan',25,'London')")
t3 = Timings(title = "dict",  setup = "pass", 
                              statement = "p = {'name' : 'Susan', 'age' : 25, 'address' : 'London' }")

t4 = Timings(title = "class", setup = "from myprogram import Person\np = Person('Susan',25,'London')", 
                              statement = "s = p.getDetails()")
t5 = Timings(title = "slots", setup = "from myprogram import PersonSlots\np = PersonSlots('Susan',25,'London')", 
                              statement = "s = p.getDetails()")
t6 = Timings(title = "dict",  setup = "p = {'name' : 'Susan', 'age' : 25, 'address' : 'London' }", 
                              statement = "s = p['name'] + ',' + str(p['age']) + ',' + p['address']")

print "\n*** Creating instances ***"    
t1.run(10000000)
t2.run(10000000)
t3.run(10000000)
print "\n*** Calling methods ***"
t4.run(10000000)
t5.run(10000000)
t6.run(10000000)

