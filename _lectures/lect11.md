---
num: "Lecture 11"
desc: "File I/O, Midterm 2 Review"
ready: true
date: 2018-02-27 14:00:00.00-7:00
---

```
# CS 8, 2-27-18

''' Files
    - FILES are a valuable tool to help us solve many
    types of problems.

FILES give us PERSISTENCE
    - So far, we've been running our programs in IDLE and
    putting our code into a file.
    - Between each run, our data is cleared and everything
    has to be reloaded again.
    - With PERSISTENCE, our data can be "saved" between
    each program execution.

FILE BASICS
    - We can read from files
    - We can store files in many different forms
        - Examples: .xls, .docx, .pdf, .jpg, ...
        - For this class, we'll just deal with "plain text"
        files (.txt)
        - These CHARACTERS are represented in something called
        ASCII (American Standard Code for Information Interchange)
        - This was dominant / simple way of representing text
        where each character is 8 bits long
        - UTF-8 is the most popular format in today's web browsers
        - Allows us to represent MANY characters from multiple
        languages
    File: A document
    Directory: A folder containing files and other folders
    File System: Collection of all the files and folders on the
        computer
    For this class, we'll deal with reading and writing files
    that are in the same directory as our .py file (known as
    our "working directory"
        - This makes our lives much easier

FILE I/O:
    - I/O stands for input / output
    - We read data from a file into our program.
    - We write data from our program into a file.
    - Steps for File I/O
        1. Open the file (creates a "connection" between your
        program and the file).
            - Choose if the connection will be for reading,
            writing, or appending to a file.
        2. Read the data / write the data
        3. Close the file (close the "connection"). This should
        to be done once per file.

Common ways to read data from files
    1. read() method - reads the entire file into one string
        - Good for small data (large files may be too big to
        store into memory)
    2. read(n): Read the next n characters from the input
        - Better for larger files since you only need to store
        n characters in memory at a time.
    3. readline(): Reads everything from the current position
        to the next '\n' (or to the end of the file, 'EOF'). If
        nothing left to read, .readline() returns an empty string.
    4. readlines(): Reads all the lines in the file and returns
        a list.
    5. for a_line in infile:
        - a_line represents a line in the file, infile is the
        open file.
'''

'''
# Example reading from 'example.txt'
infile = open('example.txt', 'r')
data = infile.read()
print(data)
infile.close()
'''
'''
# Example writing to a file 'example_2.txt'
outfile = open('example_2.txt', 'w')
outfile.write("This is Line1\nThis is Line2\nThis is Line3")
outfile.close()
'''
'''
# Create a list of lines in the file
infile = open('example.txt', 'r')
datalines = infile.readlines() # returns a list of strings
print(datalines)
infile.close()
'''
'''
# Write "overwrites" the existing file
outfile = open("example.txt", 'w')
outfile.write("Something new!\n")
outfile.write("Another line!")
outfile.close()
'''
'''
# Append to an existing file
outfile = open("example.txt", 'a')
outfile.write("Something else!\n")
outfile.write("Yet another line.")
outfile.close()
'''
'''
# read(n)
infile = open("example.txt", 'r')
data = infile.read(3)
print(data)
data = infile.read(6)
print(data)
infile.close()
'''
'''
# readline example
infile = open("example.txt", 'r')
line = infile.readline()
print(line)
line = infile.readline()
print(line)
infile.close()
'''
'''
# Example of copying / writing to another file
infile = open('example.txt', 'r')
outfile = open('copy.txt', 'w')
for line in infile:
    outfile.write(line)
infile.close()
outfile.close()
'''
'''
Midterm 2 Review

Accumulator Pattern
- count elements
- keep track of certain conditions (largest, smallest, min, most, ...)
- reconstruct / accumulate lists of things

Double (nested) for loops
- for within a for loop (or while)...
- Good for traversing a list within a list, or chars of strings
within a list

While Loop
- while BOOLEAN_EXPESSION:
    STATEMENT(S)
- can loop forever
- break, continue, pass

2D lists
- Lists within lists, represents data in a "grid"
- screen of pixels, tic-tac-toe

String functions
- find, startswith, endswith, count, replace, upper, lower,
...
- String formatting
    - .format method # {:} ...

Random
- randrange, shuffle, sample, ...
'''
```








