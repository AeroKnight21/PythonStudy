student = {'name': 'Joel', 'age': '12', 'courses': ['Math', 'CompSci']}

print(student)

student['phone'] = '555-5555'

print(student)

student['name'] = 'Jill'

print(student)

print(student['courses'])

print(student.get('name'))

print(student.get('adress', 'Not Found'))

print(student)

student.update({'name': 'Bill', 'age': 26, 'phone': '777-7777'})

print(student)

del student['age']

print(student)

student['gender'] = 'male'

print(student)

gender = student.pop('gender')

print(gender)

print(student)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

for key, value in student.items():
    print(key, value)

# Exercise

phone = input("Phone: ")
digits_mapping = {"1": "One",
                  "2": "Two",
                  "3": "Three",
                  "4": "Four",
                  "5": "Five",
                  "6": "Six",
                  "7": "Seven",
                  "8": "Eight",
                  "9": "Nine"
}
output = ''
for ch in phone:
    output += digits_mapping.get(ch, "!") + ' '

print(output)
