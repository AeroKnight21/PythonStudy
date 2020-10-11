"""
LEGB
local, enclosing, global, built-in
"""

# Built-in
import builtins

print(dir(builtins))

def my_min():
    pass

m = min([5,1,4,2,3])
print(m)

# Local/Global
x = 'global x'


def test(z):
    x = 'local x'
    y = 'local y'
    print(y)
    print(z)


test('local z')
# print(x)

# Enclosing
def outer():
    x = 'outer x'
    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()