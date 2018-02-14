# lab04.py

# Student(s): (insert name and perm number here)

# This file contains several incomplete function definitions with stub
# values. Lab04_tests.py have tests to check if the functions are correct.
# Your assignment is to complete each function according to the
# functions' descriptions.
#
# Once you complete a function, you can run pytest on the tests defined
# in lab04_tests.py to see if your functions are working correctly.

def totalCharacters(listOfStr):
    '''
    (10 points)
    Function that takes in a list of strings (listOfStr) and returns
    the number of characters for all characters in the strings in
    listOfStr.
    - Returns -1 if listOfStr is not a list type or if any element in
    listOfStr is not a string type.
        - Note: There are many ways to do this and returning -1 is known
        as a SENTINAL value, which is a value that should not occur. In
        this case, having -1 as a character count signals the caller of
        the function that something went wrong (since it doesn't make
        sense for a character count to be negative). This is not the only
        way to communicate an incorrect state (there are better ways to
        handle errors like this), but we will use a sentinal value for
        this function.
    '''
    return "stub"


def factorial(n):
    '''
    (10 points)
    Function that takes an integer and returns the value of n factorial
    (n!). 
    - If n is negative or not an int type, return the sentinal value
    of -1
    - Your solution should use a for loop and not use functions from
    python's math module.
    - Hint: note that 0! = 1. You may have to adjust your range in your
    for loop to account for this.
    '''
    return "stub"


def maxNum(listOfNums):
    '''
    (20 points)
    Function that takes in a list of numbers (listOfNums) and returns
    the maximum value in the list.
    - Returns the None type if listOfNums is not a list, listOfNums
    does not have elements in the list, or an element in listOfNums is
    not a numerical type (int or float).
        Note: This is an example of using python's None type as a
        sentinal value.
    - Your solution should use a for loop and not use the max() function.
    - Hint: You can assign a default maxValue variable as the 1st element
    of listOfNums if valid. You can then iterate through listOfNums and
    compare the current maxValue with each element in the list, updating
    maxValue if necessary.
    '''
    return "stub"


def indexOf(value, listOfValues):
    '''
    (20 points)
    Function that takes in a value (of any type) and a list of values
    containing any type (listOfValues). Returns the index in the list of
    the first match between value and an element in listOfValues.
    - Returns None if listOfValues is not a list type.
    '''
    return "stub"


# Item namedtuple definition used for the next two functions
# Name is the name of an item, price is the price of an item, and
# purchased is the number of items sold.
from collections import namedtuple
Item = namedtuple("Item", "name price purchased")

def unpopularItems(listOfItems):
    '''
    (20 points)
    Function that takes in a list of Items. Returns a new list of items
    containing the items that had 0 purchases.
    - Note: We've seen something similar to this in the last lab. Think
    of using .append to add items to your resulting list when the amount
    purchased is 0.
    '''
    return "stub"


def updatePrice(pricePercent, listOfItems):
    '''
    (20 points)
    Function that takes a pricePercent value and a list of Items.
    Returns a list with updated Items in listOfItems with the original
    price changed by pricePercent.
        - For example, if an item is 1.00 and pricePercent is 50, then
        the updated price is 1.50. If an item is 1.00 and pricePercent
        is -50, then the resulting price is 0.50.
    - Hint: Recall that namedtuples are IMMUTABLE types and we cannot
    simply change a namedtuple attribute. See lecture 04 on how we can
    update namedtuple attributes using the ._replace method or
    constructing a new namedtuple object.
    '''
    return "stub"
