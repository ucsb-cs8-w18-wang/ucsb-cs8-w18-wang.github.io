---
num: "Lecture 8"
desc: "Iterating through lists, Accumulator Pattern, Nested Loops, While Loops"
ready: true
date: 2018-02-13 14:00:00.00-7:00
---

```
# CS 8, 2-13-18

''' Midterm
    - Average 54.92 / 68
    - Medium: 55.25
    - std: 5.94

- Common mistakes on the midterm
    - print("some string") # removes the quotations when
    outputting to the console
    - 1 / 1 = 1.0 # division returns a float type
    - return statements
        - A function immediately exits whenever it reaches
        a return statement.
        - A function can only return one value (but the
        value could be a collection (such as a list) that
        contains many values.

- Accumulator Pattern
    - Have seen this already in lab, but let's go into more
    detail.
    - Useful for "accumulating" something while traversing
    a collection.
        Example: Count the number of times, count the
        number of characters in a string, ...

#Example

listOfStrings = ["this", "is", "a", "list", "of", "strings"]
numList = [8,2,6,4,0]

def computeLengthManually(someList):
    """ count the number of items in the list manually """
    elements = 0
    for e in someList:
        elements += 1 # elements = elements + 1
    return elements

print(computeLengthManually(listOfStrings))
print(computeLengthManually(numList))
'''
"""
# Another Example
sentence = '''
This is a pretty long sentence, with many many words and
letters, and a bad example of what good sentence structure
would look like, so don't do this
'''
print(sentence)

print(sentence.split())
# split() "splits" a string into a list of strings
# separated by ' ', '\n', or '\t' (whitespace)

print(sentence.split(','))
# split(',') "splits" the string into a list of strings
# separated by ','
# Notice that commas are removed from the actual values
# May be useful for comma separated value (csv) formats

# strip() string method
# Removes the whitespace at the beginning and end of
# strings
x = "     abc    "
print("---" + x + "---")
print("---" + x.strip() + "---") # removes whitespaces at ends

y = "--,!'fj,ka--"
print(y.strip("-,!'")) # removes these characters from
                       # the beginning and end
"""
"""
sentence = '''
This is a pretty long sentence, with many many words and
letters, and a bad example of what good sentence structure
would look like, so don't do this
'''

# Example
def countLongWords(someString):
    ''' counts words longer than 5 characters '''
    counter = 0
    words = someString.split()
    for w in words:
        if len(w) > 5:
            counter += 1
    return counter

print(countLongWords(sentence))
"""

''' Nested Loops
- Depending on how data is organized, it's common to see
loops within loops.
- For example, given a list of strings, we may want to
manually count how many vowels exist throughout the list
'''
'''
# Nested-for loop example
listOfStrings = ["this", "is", "a", "list", "of", "strings"]

def countVowels(strList):
    """ Count vowels in list of strings """
    vowels = "AEIOUaeiou"
    numVowels = 0
    for s in strList:   # s is an str element in strList
        for c in s:     # c is a character in s
            if c in vowels:
                numVowels += 1
    return numVowels

print(countVowels(listOfStrings))
'''

''' While Loop
- Another looping construct we'll use in this class
    - While loops are used when you want to repeat a set
    of statements indefinitely
    - Note: the number of times that goes through the
    loop is independent on the number of elements in a
    collection.
    - Examples: Web servers, OSes, ...

Syntax:
while BOOLEAN_EXPRESSION:
    STATEMENT(S)

Semantics:
- if BOOLEAN_EXPRESSION is true, perform statements in the
body of the loop
- if BOOLEAN EXPRESSION is false, skip the loop entirely
and continue execution.

- Keyword "break"
    - It's possible to exit the loop and jump out of it
    using the break statement

while True: #Loop forever - common in some UI/Game/servers
    # Somewhere in the middle, we can change our mind
    # and check to see if we want to break out
    if BOOLEAN_EXPRESSION:
        break
    ...
'''
'''
# Example:
x = 0
while True:
    x = x + 1
    print("Start of while body, x =", x)
    if x > 3:
        break
    print("End while body, x =", x)
    print("------")
print("outside of while loop")
'''
'''
- Keyword "continue"
    - It's possible to check and see if you want to
    continue executing the loop body, or go back
    and evaluate.
'''
# Example
x = 0
while True:
    x = x + 1
    print("Start of while body, x=",x)
    if x % 2 == 0: #if x is even
        continue
    if x >= 5:
        break
    print("End of while body, x=", x)
    print("------")
print("Outside while loop")
```



