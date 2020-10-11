message = "Hello World"

print("Hello World")

print(message)

print(len(message))

print(message[6])

print(message[0:5])

print(message[:5])

print(message[6:])

print(message.lower())

print(message.upper())

print(message.count('l'))

print(message.count('World'))

print(message.find('World'))

print(message.count('Universe'))

new_message = message.replace("World", "Universe")

print(new_message)

greeting = 'Hello'
name = 'Joel'

greet = greeting + ', ' + name + '. Welcome!'
greetf = "{}, {}. Welcome!".format(greeting, name)
greeretf2 = f"{greeting}, {name}. Welcome!"
greetf2 = f"{greeting}, {name.upper()}. Welcome!"

print(greet)
print(greetf)
print(greetf2)

print(dir)

course1 = '''
Hi John,

Here is our first email to you

Thank you,
The Support Team
'''
print(course1)

another = message[:]

print(another)

# exercise
name = 'Jennifer'
print(name[1:-1])
# Done

first = 'John'
last = 'Smith'

message = first + ' [' + last + ']' + ' is a coder'
print(message)
msg = f'{first} [{last}] is a coder'
print(msg)

course = 'Python for Beginners'
print(len(course))

print(course.upper())

print(course)

print(course.lower())

print(course.find('P'))

print(course.replace('Beginners', 'Absolute Beginners'))
