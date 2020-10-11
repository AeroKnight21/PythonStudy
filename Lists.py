courses = ['History', 'Math', 'Physics', 'ComputerSci']
courses2 = ['Art', 'Education']
nums = [1, 5, 2, 4, 3]
course_str = ', '.join(courses)
course_str2 = ' - '.join(courses)
new_list = course_str.split(' - ')

print(course_str)
print(course_str2)
print(new_list)

print(courses)

print(len(courses))

print(courses[0])

print(courses[2])

print(courses[-1])

print(courses[-3])

print(courses[0:2])

print(courses[:3])

print(courses[1:])

courses.append('Gym')

print(courses)

courses.insert(0, 'Music')

print(courses)

courses.insert(0, courses2)

print(courses)

print(courses[0])

courses.extend(courses2)

print(courses)

courses.remove('Math')

print(courses)

popped = courses.pop()

print(popped)
print(courses)

courses.reverse()

print(courses)

print(nums)

nums.sort()

print(nums)

nums.sort(reverse=True)

print(nums)

sorted_nums = sorted(nums)

print("this is a different list. " + str(sorted_nums))

print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('ComputerSci'))
print(courses)

courses.insert(6, 'Math')
print(courses)

print('Math' in courses)
print('Spanish' in courses)

courses.remove('Art')
print(courses)

for item in courses:
    print(item)

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=3):
    print(index, course)

# Lists are Mutable

# Exercise

numbers = [1, 2, 3, 4, 5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# Exercise

dupe = [2, 2, 4, 6, 3,  4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)