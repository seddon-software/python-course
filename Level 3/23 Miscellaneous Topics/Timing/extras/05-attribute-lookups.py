from timings import Timings

t1 = Timings(title = "attribute lookup", setup = "from myprogram import Point; p = Point(15, 33)", 
                                         statement = "distance = p.x * p.y")
t2 = Timings(title = "using locals",     setup = "from myprogram import Point; p = Point(15, 33); x = p.x; y = p.y", 
                                         statement = "distance = x * y")

Timings.titles()
t1.run(1000000)
t2.run(1000000)
t1.run(5000000)
t2.run(5000000)

