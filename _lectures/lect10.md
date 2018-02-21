---
num: "Lecture 10"
desc: "More on String Formatting, Random"
ready: true
date: 2018-02-20 14:00:00.00-7:00
---

```
# CS 8, 2-20-18

# Some tools for the labs
# min, max, round

print(max(15.7,2,16.2,8))
print(min(16.2,6))
print("---")
print(round(14.9999999999))
print(round(15.5))
print(round(15.4999999999))

# STRING FUNCTIONS
# We've seen several of these - .split(), .strip()
# We'll introduce some more...


s = "CS 8: Intro to Programming"
'''
print("Where does the first 'mm' occur in s?")
print(s.find("mm"))
print(s.find("jfklahgl"))

text = """This
string
has
multiple
lines"""

first_newline = text.find("\n")
print("First newline position:", text.find("\n"))
print("First line of text:", text[:first_newline])
print("String after first newline:", text[first_newline + 1:])
'''
'''
# .startswith method
print("Check if s starts with 'CS':", s.startswith("CS"))
print("Check if s starts with 'Computer':", s.startswith("Computer"))

# .endswith method
print("Check if s ends with 'P':", s.endswith("P"))
print("Check if s ends with 'inG':", s.endswith("inG"))
print("Check if s ends with 'ing':", s.endswith("ing"))

# .count method
print("Times 'm' is in s:", s.count("m"))
print("Times 'i' is in 'Mississippi':", 'Mississippi'.count('i'))
MS = "Mississippi"
print("Times 'ss' is in 'Mississippi':", MS.count('ss'))

# .replace method
print("Change all 'i' to '!' in 'Mississippi':", MS.replace("i", "!"))
print("Change all ':' to '#' in s:", s.replace(":", "#"))
print("Remove all 'i' in 'Mississippi':", MS.replace("i",""))

# Strings are immutable (these methods won't change the string)
print(s)
print(MS)

# Change the value with reassignment
s = s.replace("m", "M")
print(s)

# upper / lower case
print(s.lower())
print(s.upper())
print(s) # still didn't change
'''

# Examples of String formatting

price = 18.00
print("The price is ${}. That's cheap!".format(price))
print("The price is ${}. {}.".format(price,"wow!"))
print("{3:} {2:} {1:} {0:}".format('a','b','c','d'))

''' Format specification:
{ : }. Left side of colon say which argument to place into {}

To the right we specify a FIELD WIDTH (i.e., how many spaces/
columns on the screen to devote to this
'''
'''
print("-->{}<--".format(price))
print("-->{:20}<--".format(price))
print("-->{:20}<--".format("18"))
# We can use '>' or '<' to justify left or right
print("-->{:<20}<--".format("18"))
print("-->{:>20}<--".format("18"))
# we can use '^' to center.
print("-->{:^20}<--".format("18"))
'''
print("-->{:20.2f}<--".format(price))
# without 'f' , price appears in scientific notation

# More examples
price = 12345.6
print("-->{:10.2f}<--".format(price))
print("-->{:6.2f}<--".format(price))

# can identify specific types that should be expected with
# 's'- string, 'd' - int, 'f' - float
name = "Chris Gaucho"
age = 21
print("Name is {:12s}; age is {:2d}; price is ${:0.2f}".format(name,age,price))
print("Name is {:12}; age is {:2}; price is ${:0.2}".format(name,age,price))
# still works if s,d,f is not included, but removing 'f' will look strange

# Random
# Useful for many applications (ESPECIALLY GAMES!)
# Games use Random Number Generator (RNG) defines unpredictable
# behavior (Lottery, Dice, Random Drops, Simulations, ...)

# Python has a random module that has a random number generator
# randrange(x,y) is a function that produces a random integer
# including x up to (but not including) y.

from random import randrange

def rollDie():
    return randrange(1,7)

diceTally = [0,0,0,0,0,0,0] # 7 because diceTally[0] is not used

for rolls in range(200):
    value = rollDie()
    diceTally[value] += 1

def printDistribution(distributionList):
    for x in range(1,7):
        #print("{:2d}: ".format(x), distributionList[x])
        print("{:2d}: ".format(x), '*' * distributionList[x])

printDistribution(diceTally)
```