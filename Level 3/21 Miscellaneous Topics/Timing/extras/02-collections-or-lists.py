from timings import Timings

t1 = Timings(title = "collections", setup = "import collections; s = collections.deque()",
                                    statement = "s.appendleft(100)")
t2 = Timings(title = "lists",       setup = "s = []", 
                                    statement = "s.insert(0,100)")

Timings.titles()
t1.run(100000)
t2.run(100000)
t1.run(200000)
t2.run(200000)
