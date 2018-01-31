---
num: "Lecture 5"
desc: "Boolean Expressions, Conditionals"
ready: true
date: 2018-01-30 14:00:00.00-7:00
---

# Topics
* Remote Login via ssh instruction links

* <https://ucsb-cs8.github.io/topics/csil_via_macos/>

* <https://ucsb-cs8.github.io/topics/csil_via_windows/>

```
# CS 8, 1-30-18

''' Pair Programming
    - A popular and effective way for students to learn
    programming.
    - Pair programming is highly adopted in courses
    (and even industry).
        - Don't just split up the work like "you do the
        1st half and I do the 2nd half"
        - This may be OK in software dev teams, but not
        OK from a learning perspective.
        - Pairs should work in sync with each other such
        that both students learn all the material.
    - Format of pair programming
        - One student is a DRIVER that controls the
        keyboard and types out the code.
        - One student is a NAVIGATOR that asks questions
        and provides deeper insight.
        - Both DRIVERS and NAVIGATORS contribute to
        solving the problem together.
        - DRIVER and NAVIGATOR switch off periodically
            - Both students can write out the code.
    - Strong-style pair programming
        - Similar to traditional pair programming, BUT
        - NAVIGATOR must communicate what the DRIVER types
        - "For an idea to go from you head into the computer,
        it MUST go through someone else's hands"
    - Working with a partner for Lab02 is optional.
        - Gradescope allows each submission to add a
        "group member"
        - Be sure to add a group member FOR EACH submission.
    - Some general advice with working in groups
        - Don't flake out on your partner!
'''
''' Recall - Booleans
    - Boolean values are a special type that evaluates
    to either True or False
    - BOOLEAN EXPRESSIONS are statements that evaluate
    to True or False

#Example
print(4 < 6)
print(4 == 4)
print(4 != 4)
print(4 >= 5)
print("Rich" in "Richert")

# Boolean Algebra
x = True
y = False
print(not x)
print(not y)
print(x and y)
print(x or y)
'''

''' Conditional Statements
- The ability to tell the computer to perform one thing
in a situation vs another thing in another situation.
- It enables programmers to customize their program's
behavior
- The basic construct to tell a program to do one thing
or another is an IF statement

Syntax:
if BOOLEAN_EXPRESSION:
    STATEMENT(S)

- Evaluates the boolean expression (True or False)
    - If True, execute the statement(s)
    - If false, skip the statement(s) and continue
    execution.
    - Indentation in Python is VERY IMPORTANT!
    - It tells python which statements are executed in
    certain conditions

# Example
milesDriven = 150
print("Should you pull over and fill up your gas tank?")
if milesDriven > 200:
    print("Yes, you need gasoline") # part of the condition
print("Drive safe") # not part of condition since not indented

- What if we wanted to do something in the event that the
boolean condition is False?

if BOOLEAN_EXPRESSION:
    STATEMENT(S) #1
else:
    STATEMENT(S) #2

- Evaluate the boolean expression (True or False)
- If True, execute STATEMENT(S) #1
- If False, skip STATEMENT(S) #1 and execute STATEMENT(s) #2
'''
'''
milesDriven = 50
print("Should you pull over and fill up your gas tank?")
if milesDriven > 200:
    print("Yes, you need gasoline")
else:
    print("Nope, you can keep driving")
print("Drive safe")
'''
'''
- You can nest expressions / functions / etc. to form
your boolean expression
'''
'''
# Example
if int(input("What's your age? ")) >= 21:
    print("You can drink alcohol, but do so responsibly")
else:
    print("Can't drink alcohol yet - how about some OJ")
print("Enjoy the party")
'''
''' Repetition and Loops
- Besides conditions, another useful task for a program
to do is repeat the same thing over and over and over ...
- A FOR loop is like looping through a collection and doing
something for each item.

Syntax
for VARIABLE in COLLECTION:
    STATEMENT(S)

- Assigns an element in the collection to the variable (starts with 1st item)
	- Executes STATEMENT(S)
- Assigns the next item in the collection to the variable
	- Executes STATEMENT(S)
- Continues program execution when there are no more items in the collection.

'''
# A simple example with a "FOR" loop
name = "Richert"
for c in name:
    print(c) # prints each character in name on a single line

# Example with multiple types in a list (collection)
list = [[1,2], "Richert", 4.2, 100, True]
for var in list:
    print(var)
    print("------")

print("out of for loop")
print("continuing...")
```
    
    






