import math

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

# Comparisons
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num1 = 1
num2 = 2
num3 = 3

print(num1 == num2)
print(num1 != num2)
print(num3 > num2)
print(num3 < num2)
print(num1 <= num2)
print(num1 >= num2)

print(3+2)
print(3-2)
print(3* 2)
print(3/2)
print(3//2)
print(3**2)

print(2%2)
print(3%2)
print(4%2)
print(5%2)

# Order of Operations
print(3 * 2 + 1)
print(3 * (2 + 1))

# Increments
num = 1

num = num + 1
num += 1

num2 = 1

num2 *= 10

print(num)

print(abs(-3))

print(round(3.75, 1))

num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)

x = 2.9
print(round(x))
print(abs(-2.9))

print(math.ceil(2.9))
print(math.floor(2.9))