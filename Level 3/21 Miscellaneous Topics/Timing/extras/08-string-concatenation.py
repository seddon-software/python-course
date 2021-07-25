from timings import Timings

t1 = Timings(title = "+=",             setup = "s = ''", 
                                       statement = "for i in range(100000000): s += 'a'")
t2 = Timings(title = "array",          setup = "import array",
                                       statement = "s = ''.join(array.array('c', ['a']*100000000))")
t3 = Timings(title = "comprehensions", setup = "pass",
                                       statement = "s = ''.join(['a' for n in range(100000000)])")

Timings.titles()
t1.run(1)
t2.run(1)
t3.run(1)
