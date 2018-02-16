---
num: "Lecture 9"
desc: "More on while Loops, 2D Lists"
ready: true
date: 2018-02-15 14:00:00.00-7:00
---

```
# CS 8, 2-15-18

''' Recap
- While loops
- Break statement
- Continue statement

- The "pass" statement
    - Considered a "no-op" (no-operation). Doesn't do
    anything, but some functions or conditions require
    a statement for legal syntax.

# Example
def f():
    pass

print(f())

# Note: exiting a function without a return statement
# is OK, but the return value is None if the function
# doesn't return anything.

x = 6
if x > 5:
    pass # if this is removed, then a syntax error!
else:
    print(x, "<= 5")
print("continue execution...")

# In general, I find that I rarely use "pass" statements
# we can write code to avoid having pass statements.
'''

'''
# Example - A number guessing game

magicNumber = 40
guess = input("Guessing Game!\nPlease enter an int \
between 0 - 100 (type 'exit' to end game): ")

while True:
    if guess == "exit":
        print("Game over!")
        break
    number = int(guess)
    if number < 0 or number > 100:
        guess = input("Invalid number. Please try again: ")
        continue
    if number < magicNumber:
        guess = input("Too small. Please try again: ")
        continue
    if number > magicNumber:
        guess = input("Too big. Please try again: ")
        continue
    if number == magicNumber:
        print("Winner winner, chicken dinner!")
        print("You guessed", magicNumber)
        break
print("Done.")
'''

''' Two-dimensional Lists (2D Lists)
- Normal Lists: One number is used to index an item
    - Think of it as a straight line from 0 to N-1 elements
- 2D Lists
    - Think of it as a table where two numbers (two
    dimensions), represented with a row and column
    can index the items.
    - Elements can have some logical mapping with respect
    to the row / column value

- Conceptual example
    - Computer screens can be represented in a Grid of
    pixels
    - Basic color screens can have color values
    (Red, Green, Blue) for different colors
    - Monochrome screens (black and white) can be represented
    as a Grid of black / white pixels
'''
def new_screen(rows, columns):
    ''' Create and return an empty screen. A list of
    rows, with each row being a list of pixels going across
    that row. Initially, all pixels will have the value
    of 0 (representing black)
    '''
    result = []
    for r in range(rows):
        result.append([0] * columns)
    return result

'''
print(new_screen(2,3))
assert new_screen(2,3) == [ [0,0,0], [0,0,0] ]
print(new_screen(200,50))
'''
screen = new_screen(10,5)
print(screen)

def print_screen(grid):
    for row in range(len(grid)):
        # Print one row
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                pixel = ' # '
            else:
                pixel = '   '
            print(pixel, sep='', end='')
        print() # Newline for the end of the row
    return

'''
print_screen(screen)
print()
screen[2][3] = 1 # set a specific pixel
print_screen(screen)
'''

#print(screen)

def set_row(grid, rownum, value):
    ''' Change the screen so that the specified row has the
        specified value all the way across.
    '''
    for col in range(len(grid[rownum])):
        grid[rownum][col] = value
    return

'''
set_row(screen, 3, 1)
print_screen(screen)
set_row(screen, 7, 1)
print("-----")
print_screen(screen)
'''

def set_column(grid, column, value):
    ''' Change the screen in place so the specified column has the
        specified value all the way down
    '''
    for row in range(len(grid)):
        grid[row][column] = value
    return

screen2 = new_screen(10,20)
print_screen(screen2)
print("-----")
set_column(screen2, 7, 1)
set_column(screen2, 17, 1)
set_row(screen2, 5, 1)
print_screen(screen2)
```