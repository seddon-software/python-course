from collections import deque

d = deque([1,2,3,4,5])
print(d)

d.append(10)
d.appendleft(-10)
print(d)


d.extend([99,99,99])
d.extendleft([-99,-99,-99])
print(d)



1