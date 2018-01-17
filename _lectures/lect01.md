---
num: "Lecture 1"
desc: "Introduction"
ready: true
date: 2018-01-16 14:00:00.00-7:00
---

Please read through syllabus for logistics of the course:
https://ucsb-cs8-w18-wang.github.io/info/syllabus/

```
# CS 8, 1-16-18

'''
In python, we can separate ENGLISH text ("comments") from source
code by:
    - Preceeding them with a pound, number, sharp, hashtag,...
    - enclosing in triple single (or double) quotes.

Q: What are computers used for?
    - Gaming
    - Searching / Browsing
    - eCommerce
    - Word processing
    - Social Networks / communication
    - Netflix
    - Big data
    - ...

Basic Terminology
    - PROCESSOR: Does computations
    - MEMORY / STORAGE: Contains information to act on or instructions
        to execute
    - PERIPHERALS: Keyboards, mouse, monitors, speakers
    - SOFTWARE is the instructions that the processor follows
        - Think of a chef following a recipe.
        - Hardware: Ingredients, knives, cutting boards, fridge, ...
        - Software: Recipe
        - COMPUTER PROGRAM is a set of instructions written in terms
            a computer can understand and follow.
        - ALGORITHM is a step-by-step procedure to do something
            - Chef's recipe is an algorithm
            - A computer program contains algorithms
            - CODE or SOURCE CODE refers to the text containing algorithms
                that the computer understands in order.

VARIABLES
    - Variables are useful for storing values of any type.
    - There are many "types" in Python, programmers can also create
        custom types.
    - Types are important depending on what you need to do with the data.
        - Some types support certain functionality while others don't.
        - Using certain types can affect the performance of your program.
    - Names of variables must ...
        - Start with a letter or underscores (the former is more common)
        - Remaining letters in variable names can consist of letters, numbers,
            or underscores
        - Names are case-sensitive ("name" and "NAME" are considered two
            different variables).
'''

x = 10
print(x)
x = x * 10
print(x)
```