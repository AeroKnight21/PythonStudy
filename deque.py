import collections
from collections import deque

d = deque("hello", maxlen = 5) # maxlen makes it have a max length of 5 as stated
print(d)

d.append('4')
d.appendleft(5)
print(d)

d.popleft()
print(d)

d.clear()

d.extend('456')
d.extend('hello')
d.extendleft('hey')
print(d)

d.rotate(1)
print(d)