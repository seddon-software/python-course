from timings import Timings

t1 = Timings(title = "using xrange", setup = "total = 0", 
                                     statement = "for x in xrange(100 * 1000 * 1000): total = total + x")
t2 = Timings(title = "using range",  setup = "total = 0", 
                                     statement = "for x in range(100 * 1000 * 1000): total = total + x")

Timings.titles()
t1.run(1)
t2.run(1)

