'''
We can use the pstats module to extract statistics from the profiler.
'''

import profile, pstats, os


class memoize:
    def __init__(self, function):
        self.function = function
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = self.function(*args)
            return self.cache[args]

@memoize
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

def fibonacci_seq(n):
    seq = [ ]
    if n > 0:
        seq.extend(fibonacci_seq(n-1))
    seq.append(fib(n))
    return seq

# Create stats
if not os.path.exists('stats'): os.mkdir('stats')

# generate statistics
profile.run('print(fibonacci_seq(20))' , 'stats/fibonacci')

# display statistics
stats = pstats.Stats('stats/fibonacci')
stats.strip_dirs()

# sort the statistics by the cumulative time spent in the function
stats.sort_stats('cumulative')
stats.print_stats()

# sort the statistics by the total time spent in the function
stats.sort_stats('time')
stats.print_stats()


