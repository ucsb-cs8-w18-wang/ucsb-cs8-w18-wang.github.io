---
num: "Lecture 7"
desc: "Midterm 1 Review"
ready: true
date: 2018-02-06 14:00:00.00-7:00
---

```
# CS 8, 2-6-18

''' Midterm 1 Review

- Logistics
    - Bring their studentID and a writing utensil
        - preferably ink or dark led
    - No electronic devices
    - No book
    - No notes

- Format
    - Will be a mix of questions
    - A lot of reading code / writing output
        - You need to tell me what Python will output
    - Some short answer
    - Some fill in the blank
    - Some check all that apply
    - Complete a function definition

Python Data Types
    - int, float, bool, list, tuples, namedtuples
    (custom)
    - type(x)
    - print("str") # print() removes quotes, but
    quotes are necessary to express string types
        - difference between "2" and 2.

Arithmetic operators
    - +, -, *, /, ** %, ...
    - Depending on the operator, different types
    can be returned
        - 2 / 2 # returns a float
        - 2 * 2 # integer
        - 2.0 * 2 # float

Python Functions
    - print, len, str, int, float, input, ...

Comparison operators
    - ==, !=, >=, <=, <, >

Boolean Operations
    - not, and, or
    - x < 100 and x > 90 (90 - 100)

Strings
    - Collection of characters
    - indexing [1], [-1],
    - slicing [1:3]
        - "UCSB"[1:3] # 'CS'
    - Indexing errors
        - "UCSB"[4]
    - Concatenation +
    - Multiply *
    - ...

Collections
    - Lists (Mutable)
        - Functions (.append, .sort, .pop, ...)
    - Tuples (Immutable)
    - in operator (check if something is in a collection)

Functions
    - Defining a function: def NAME(PARAMETER(S)):
    - Indentation of statements within functions
    - Return statements
        - returning a value vs. returning 'None'

Namedtuples
    - Defining / Modeling objects with namedtuples
    - Constructing namedtuples
    - Accessing namedtuples with attribute's name
    - Immutable

Testing
    - pytest,
    - pytest functions start with "test_" with assert
    - Won't require command line knowledge (for midterm1)

Conditional Statements
    - if, else, elif (else if)

For Loops
    - for VARIABLE in COLLECTION:
        STATEMENT(S)
    - range
        - range(4), range(2,4), range(1,4,1)

Nested Control Structures
    - for within an if within another if, ...
'''

from collections import namedtuple

Student = namedtuple("Student", "name perm")
s1 = x("Student1", [1,2,3])
s2 = x("Student2", [3,2,1])

print(s1.perm + s2.perm)

print(s1.perm)
print(s2.perm)
```