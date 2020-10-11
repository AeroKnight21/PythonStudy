import collections
from collections import Counter

# Containers
# list
# dict
# tuple - immuttable

# Types
#1 counter
#2 deque
#3 namedTuple()
#4 orderedDict
#5 default dict

c = Counter('hello')
print(c)
c = Counter(['a', 'a', 'b', 'c'])
print(c)
c = Counter(cats = 4, dogs = 5)
print(c)
print(c['cats'])

print(list(c.elements()))
print(c.most_common(2))

c = Counter(a = 4, b = 2, c = 0, d = -2)
d = Counter(['a', 'b', 'b', 'c',])

print(c & d)
print(c | d)
print(c+d)
print(c-d)
c.subtract(d)
print(c)
c.update(d)
print(c)
c.clear()
print(c)