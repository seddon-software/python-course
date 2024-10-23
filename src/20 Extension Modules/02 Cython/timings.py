import cython_functions as functions

def doTimings():
    t1 = Timings(title = "python (fibonacci)", setup = ("import os, sys"            "\n"
                                            "sys.path.append('../src')" "\n"
                                            "import python_functions"   "\n"
                                           ), 
                                   statement = "python_functions.fibonacci(100)")
    t2 = Timings(title = "cython (fibonacci)", setup = "import os, cython_functions",
                                   statement = "cython_functions.fibonacci(100)")
    u1 = Timings(title = "python (sumOfSquares)", setup = ("import os, sys"            "\n"
                                            "sys.path.append('../src')" "\n"
                                            "import python_functions"   "\n"
                                           ), 
                                   statement = "python_functions.sumOfSquares(1000, 4000000)")
    u2 = Timings(title = "cython (sumOfSquares)", setup = "import os, cython_functions",
                                   statement = "cython_functions.sumOfSquares(1000, 4000000)")
    
    Timings.titles()
    p_fib = t1.run(10000000)
    c_fib = t2.run(10000000)
    p_sum = u1.run(10)
    c_sum = u2.run(10)
    print(f"Fibonacci: speed up = {p_fib/c_fib:6.1f}")
    print(f"Sum of square: speed up = {p_sum/c_sum:6.1f}")


#####################################################
# code to make timings table
import timeit
class Timings(timeit.Timer):
    def __init__(self, title, setup, statement):
        self.title = title
        self.timer = timeit.Timer(stmt = statement, setup = setup)
    def run(self, number):
        t = self.timer.timeit(number=number)
        print(("{:24s}{:10d}{:8.3f}{:8.3f}".format(self.title, number, t, 1/t)))
        return t
    
    def titles():
        print(("{:24s}{:>10s}{:>8s}{:>8s}".format("code", "runs", "time", "1/time")))
        print(("{:24s}{:>10s}{:>8s}{:>8s}".format("====", "====", "====", "======")))


doTimings()


