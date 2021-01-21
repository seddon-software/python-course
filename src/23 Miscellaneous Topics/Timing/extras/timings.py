import timeit

class Timings(timeit.Timer):
    def __init__(self, title, setup, statement):
        self.title = title
        self.timer = timeit.Timer(stmt = statement, setup = setup)
    def run(self, number):
        t = self.timer.timeit(number=number)
        print "{:20s}{:8d}{:8.3f}{:8.3f}".format(self.title, number, t, 1/t)

    @staticmethod
    def titles():
        print "{:20s}{:>8s}{:>8s}{:>8s}".format("code", "runs", "time", "1/time")
        print "{:20s}{:>8s}{:>8s}{:>8s}".format("====", "====", "====", "======")

