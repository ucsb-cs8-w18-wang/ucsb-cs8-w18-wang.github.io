---
num: "Lecture 3"
desc: "Python Lists, Tuples, Namedtuples, Functions"
ready: false
date: 2018-01-23 14:30:00.00-7:00
---

```
# CS 8, 1-23-18

'''
# Some more Terminology

Syntax: Grammar, how you say something
Semantics: Meaning, what it does.

syntactically incorrect PI equals 3.14159
semantically incorrect PI = "apple"
'''

'''
Lists
    - A list is a collection of multiple values
    (similar to how a str is a collection of
    characters).
    - Note: In python, lists can be of heterogenous
    (different) types
    - Lists can have duplicate values
'''

'''
#Examples
evenNumbers = [2, "4", 6, "8"]
print(evenNumbers)
print(type(evenNumbers))
print(evenNumbers[2])
print(evenNumbers[-1])
evenNumbers.append(10)
print(evenNumbers)
#print(evenNumbers[1] + evenNumbers[2]) # ERROR
print(int(evenNumbers[1]) + evenNumbers[2])

print(evenNumbers.pop(1))
print(evenNumbers)
print(evenNumbers.pop())
print(evenNumbers)

names = ["Rick", "Morty", "Summer"]
names.sort()
print(names)
oddNumbers = [5, 3, 1]
oddNumbers.sort()
print(oddNumbers)
names.append(2018)
print(names)
names.sort() # ERROR, incompatible types 2018 is int
print(names)
'''
''' Tuples
    - A tuple is similar to a list, but with small
    (but important) differences.
    - .sort() works for lists, but not tuples
    - inherently, tuples and lists are different,
    but logically they seem the same.
    - can change an element in a list, but can't
    change them in a tuple.
'''

'''
#Examples
oddNumbers = (1, 3, 5, 7)
print(oddNumbers)
print(type(oddNumbers))
print(oddNumbers[2]) #5

oddNumbers2 = [1, 3, 5, 7]
oddNumbers2[2] = 9
print(oddNumbers2)
# oddNumbers[2] = 9 ERROR, cannot change item in tuple
#print(oddNumbers)

oddNumbers = (1, 3, 9, 7)
print(oddNumbers)
'''
''' Namedtuples
    - Package heterogenous things into a multi-
    attribute item
    - We can represent more complex data into
    specific types
    - Ex: Students
        - Name, perm, major, DOB, address, GPA,
        full-time / part-time, international, ...
    - Creating multi-attribute things is the basis
    of object oriented programming.
'''
'''
#Example on using namedtuples

# Step 1: Allow your program to use namedtuples.
from collections import namedtuple

# Step 2: Design your object
Student = namedtuple("Student", "name perm major GPA")
# Parameters of function, 1st is name of the namedtuple
# type (Student).
# 2nd parameter is a string containing the names of
# attributes

# Step 3: Create objects
s1 = Student("John Doe", 1234567, "CS", 3.5)
s2 = Student("Jane Doe", 7654321, "MUSIC", 3.9)

print("Name of s1:", s1.name)
print("Perm of s1:", s1.perm)
print("GPA of s2:", s2.GPA)
print(s1)
print(s2)
print(type(s1))
'''

''' Defining Functions
'''

# Function definition
def double(n):
    ''' Returns 2 times the parameter '''
    return 2 * n

'''
- The "def" indicates a function definition
- "double" is the name of the function
- (n) denotes the parameter(s) of a function
- name + parameters is known as a function SIGNATURE
- The actual code (instructions) (ex: return 2 * n)
is known as the function BODY
- Note: The function body needs to be indented so python
can associate the body's instructions as part of the
function's definition
- If the function returns a value, then a RETURN statement
is needed
'''
# Examples calling double()
print(double(10)) # --> print(20)
print(double(double(2))) # --> print(double(4)) --> print(8)
value = double(5) + double(6)
print(value)

print(double("2"))
print(type(double("2")))
print(double(2.5))
print(type(double(2.5)))
print(double([2,4,6]))
```
















