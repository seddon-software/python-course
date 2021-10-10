import collections

# double ended queue

# create
myDeque = collections.deque((50, 51, 52, 53))

# add to front
myDeque.appendleft(13)
myDeque.appendleft(12)
myDeque.appendleft(11)
myDeque.appendleft(10)

# add to back
myDeque.append(100);
myDeque.append(101);
myDeque.append(102);
myDeque.append(103);

# play with rotate
print(myDeque) 
myDeque.rotate(7)
print(myDeque)
myDeque.rotate(-7)
print(myDeque)

# remove items
myDeque.pop()
myDeque.popleft()
print(myDeque)


1
