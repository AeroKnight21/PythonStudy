# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)                  Doesnt Work because tuples are # Immutable
# print(tuple_2)

# Unpacking this Tuple

coordinates = (1, 2, 3)
x, y, z = coordinates

print(x)
print(y)
print(z)