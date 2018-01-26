---
num: "Lecture 4"
desc: "Immutable vs. Immutable, Python Testing"
ready: true
date: 2018-01-25 14:30:00.00-7:00
---

```python
# CS 8, 1-25-18

''' Mutable vs Immutable Types

- Lists in Python are MUTABLE (can change them in place)
'''
"""
# Example

L = [10, 20, 30, 40]
print(L)
L[2] = 300
print(L)

T = (10, 20, 30, 40)
print(T)
#T[2] = 300 # ERROR, tuples are IMMUTABLE
T = (10, 20, 300, 40)
print(T)

school = "UCSB"
#school[3] = "D" #ERROR, strings are IMMUTABLE
school = "UCSD"

from collections import namedtuple
Book = namedtuple('Book', 'title author')
b1 = Book("Harry Potter", "Rowling")
print(b1)
#b1.author = "J.K. Rowling" # ERROR, namedtuples are IMMUTABLE

''' seems intuitive to do something like changing an
attribute, but it's illegal because namedtuples are
IMMUTABLE.
'''

# Q: How can we change it?
# 1: Create a new object and reassign to variable
b1 = Book(b1.title, "J.K. Rowling")
print(b1)

# 2: Use a _replace method
b1 = b1._replace(author="Rowling")
# ._replace returns a new namedtuple and we assign back
# to the variable b1
print(b1)

''' Q: Why should we even care?
- It's the behavior of the language!
- Depending on whether or not something is immutable or
mutable, it affects how the data is treated when passing
it into a function.
'''

def add_to_end(s, i):
    ''' Returns a string with i appended to s '''
    s = s + i
    return s

name = "Richert"
print(add_to_end(name, "!"))
print(name)

# When immutable types are passed into a function, a
# COPY of the data is made and used within the function.
# Once the function returns, the immutable variable
# does not change.

def add_to_list(L, i):
    ''' Returns a list with value i appended to it '''
    L.append(i)
    return L

someList = [2, 4, 6, 8]
print(someList)
print(add_to_list(someList, 10))
print(someList)

''' When mutable values are passed into a function,
the actual value (not a copy) is modified '''

''' "None" return type '''

# If a function does not return a value, then
# the "data" is "None".

# It's up to the developer to decide if a function should
# or should not return data depending on the intention
# of using the function

# Example
# print() # print function returns None
print(print()) # print(None) -> None

# Function that returns None
def noReturn():
    ''' prints and returns nothing '''
    print("in Function noReturn()")
    # return optional, but None is returned if there isn't a value

print(noReturn())
"""
''' Python Testing '''

# Software testing is essential to ensure behavior works
# as expected.

# Assert statements can be scattered throughout your code
# If an assert statement fails (i.e. not True), then
# your program execution terminates.

"""
print("1st line")
assert 3 == 3 # Test passes, resumes execution.
print("2nd line")

def double(n):
    ''' Returns 2 * n '''
    return 2 * n

assert double(5) == 10
assert double(-2) == -4
assert double("UCSB") == "UCSBUCSB"
"""

'''pytest is a formal testing framework for python'''
def double(n):
    return 2 * n

def test_double_5():
    assert double(5) == 10

def test_double_negative():
    assert double(-2) == -4

def test_double_list():
    assert double([1,2]) == [1,2,1,2]

def test_double_string():
    assert double("UCSB") == "UCSBUCSB"

''' running pytest on functions that start with "test_" and have
an assert statement will "automate" execution of all tests and
show which ones passed and which ones failed.

- Important since this ensures software is working as expected if
many people try to modify the code at the same time
'''

''' import vs. from '''
- Not much of a difference behind-the-scene, but affects naming.

# "import" Example:
import math # gives us access to functionality in the math library

print(math.sqrt(4)) # how to use a math library function.

# "from" Example:
from math import sqrt

print(sqrt(4)) # no need to use "math." when calling sqrt function

'''
- We can "import" our own code in a file using the file name without
the ".py" extension.
- Good for organizing our code in a modular fashion.
	- Can organize all tests within a file and import functionality
	into the file running the tests.
'''

```