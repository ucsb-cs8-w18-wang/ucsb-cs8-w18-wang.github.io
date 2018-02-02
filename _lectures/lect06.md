---
num: "Lecture 6"
desc: "Nested Control Statements, Python Modules"
ready: true
date: 2018-02-01 14:00:00.00-7:00
---

# CS 8, 2-1-18

'''
# Namedtuple Review

from collections import namedtuple

Book = namedtuple("Book", "title author price") # define Book model
b1 = Book("Harry Potter", "JK Rowling", 10) # construct Book object

print(b1.title) # Use attribute name instead of b1[0]
'''
'''
# More on loops
name = "Bob"
for c in name:
    print(c)
    print("----")

print("resuming program execution")

# range function
    - range() is a function used for looping if we know
    the number of iterations we want to make.
    - range(x) returns a collection of numbers including
    0 up to (but not including) x
    - Think of range(4) as [0, 1, 2, 3]
'''
'''
# Example using range()
for x in range(4):
    print("Hello!" * x)
    print("----")
'''
'''
# Example looping from numbers 2, 3, 4, 5 using range
for x in range(2,6):
    print(x)
    print("----")

# range is similar to substring - 1st parameter defines
# the 1st number and loops up to (but not including)
# the 2nd parameter's number
'''
'''
# Example using range with steps
for x in range(0, 10, 2):
    print(x)
    print("----")
'''
'''
# Example by manually updating a variable in the loop
intList = [2,4,8,16,32,64,128,256,1024]
counter = 1
for x in intList:
    print("2 ^ ", counter, "=", x)
    counter = counter + 1
'''

''' Nested Control Structures
- We can nest statements within each control structure
(so far, we've seen if / for)
- This helps define "control" of statement execution in
different ways.
- Each block of statements within a control structure is
defined by indentation.
'''
'''
# Example
listOfNames = ["Bender", "Fry", "Leela", "Morbo"]
robots = ["Bender", "Calculon"]
humans = ["Hermes", "Fry", "Amy"]
aliens = ["Morbo", "Lurr"]

print("Checking Futurama characters with species")
for name in listOfNames:
    if name in robots:
        print(name + " is a robot")
    else:
        if name in humans:
            print(name + " is a human")
        else:
            if name in aliens:
                print(name + " is an alien")
            else:
                print("Hmm, not sure what " + name + " is")

# Functionally, this looks fine, but you can imagine the
# structure of the code becomming really messy when there
# are A LOT of possible species
# Python has the 'elif' statement that means "else if"

for name in listOfNames:
    if name in robots:
        print(name + " is a robot")
    elif name in humans:
        print(name + " is a human")
    elif name in aliens:
        print(name + " is an alien")
    else:
        print("Hmm, not sure what " + name + "is")
'''
"""
# Example: Write a function and run some assert tests

def hasOddNumber(list):
    ''' Returns True if the list has an odd number.
        Returns False otherwise
    '''
    for x in list:
        if (x % 2 != 0):
            return True
    return False

numbers1 = [2,4,5,6,8]
numbers2 = [0,10,20,30]
numbers3 = []

# Test by observation
print(hasOddNumber(numbers1))
print(hasOddNumber(numbers2))
print(hasOddNumber(numbers3))

# Test by assertions
assert hasOddNumber(numbers1) == True
assert hasOddNumber(numbers2) == False
assert hasOddNumber(numbers3) == False

# Can also define test_ functions for pytest...
"""

''' User Defined Modules
- Recall how we can import other people's code (including
your own) in our programming files
- You might notice something like if __name__=="__main__":
    - This line of code makes importing modules easier
    and doesn't include code that may not want to be reused
    - Good for importing function definitions, and not
    initializing variables, calling print statements, etc.
- For an example, see https://ucsb-cs8.github.io/ptopics/main_blocks/
'''

    






            






