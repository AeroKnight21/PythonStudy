# Comparisons
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity
# and
# or
# not
language = 'Python'

if language == 'Python':
    print("Language is Python")
elif language == 'java':
    print("Language is java")
elif language == 'javascript':
    print("Language is javascript")
else:
    print("No Match")

# It's true so it's gonna print
if True:
    print("Conditional is True")

# Not going to print
if False:
    print("Conditional is True")

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print("Bad Credentials")

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print("Bad Credentials")

if not logged_in:
    print('Please Log in')
else:
    print("Welcome")

# Checking if variables with same data are really the same
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

print(id(a))
print(id(b))

#  What python evaluates to true and false

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For Example, '', (), [].
    # any empty mapping. For Example, {}.

# Trying to evaluate it to the "False Values" and checking it out
condition = True

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
