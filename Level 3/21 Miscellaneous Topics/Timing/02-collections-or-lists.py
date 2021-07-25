from timeit import timeit

# timeit.timeit(stmt, setup, timer, number=??)
count = 100
print("collections {:0.6f}".format(timeit('s.appendleft(100)', 'import collections; s = collections.deque()', number=count)))
print("lists       {:0.6f}".format(timeit('s.insert(0,100)', 's = []', number=count)))

count = 1000
print("collections {:0.6f}".format(timeit('s.appendleft(100)', 'import collections; s = collections.deque()', number=count)))
print("lists       {:0.6f}".format(timeit('s.insert(0,100)', 's = []', number=count)))

count = 10000
print("collections {:0.6f}".format(timeit('s.appendleft(100)', 'import collections; s = collections.deque()', number=count)))
print("lists       {:0.6f}".format(timeit('s.insert(0,100)', 's = []', number=count)))

1
