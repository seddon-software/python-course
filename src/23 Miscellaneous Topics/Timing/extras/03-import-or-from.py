from timings import Timings

t1 = Timings(title = "import", setup = "import math", 
                               statement = "math.sqrt(50.0)")
t2 = Timings(title = "from",   setup = "from math import sqrt", 
                               statement = "sqrt(50.0)")

Timings.titles()
t1.run(100000)
t2.run(100000)
t1.run(500000)
t2.run(500000)

