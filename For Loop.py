nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

# nested loop
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Range in for loop
for i in range(1, 11):
    print(i)

for item in ['Mosh', 'John', 'Sara']:
    print(item)

for item in range(5, 11, 2):
    print(item)

# Exercise

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
print(f"Total: {total}")

# Nested loop pt2
for x in range(4):
    for y in range(3):
        print(f"({x}), ({y})")

# Exercise

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)