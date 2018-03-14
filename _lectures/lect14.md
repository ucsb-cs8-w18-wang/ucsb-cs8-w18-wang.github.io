---
num: "Lecture 14"
desc: "Recursion"
ready: true
date: 2018-03-13 14:00:00.00-7:00
---

[Hand traced examples in lecture](https://github.com/ucsb-cs8-w18-wang/ucsb-cs8-w18-wang.github.io/blob/master/_lectures/3_13_recursion.pdf)

```
# CS 8, 3-13-18

''' Recursion
- When a function contains a call to itself.
- We're mostly familiar with writing code in an iterative
fashion (i.e. one statement after the other).
- Many programming languages exist where it's based
purely on recursion.
    - Recursive problems are useful when the result is
    dependent on the result of its subparts.

PROPERTIES OF RECURSION
- One or more base cases that provide the "stopping"
condition
- One or more recursive valls, where the parameters are
"closer" to the base case than the function input.
'''

# Simple example: Factorial
# n! = n * (n - 1) * (n - 2) * ... * 1
# n! = n * (n - 1)!
# 0! = 1

def factorial(n):
    if n == 0:      # base case
        return 1

    return n * factorial(n-1)

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24

# What happens if we forget the base case?
def factorial2(n):
    print(n)
    return n * factorial2(n-1)

#factorial2(4)

# Infinite recursion! No stopping condition means the
# caller never returns the value.
# Program crashes - STACK OVERFLOW

# What happens if we never progress to the base case?
def factorial3(n):
    if n == 0:
        return 1
    #print(n)
    return n * factorial3(n+1)

#factorial3(4)

# Infinite recursion, the stopping condition is never
# reached.

# Example: Check if a string is a palindrome
def isPalindrome(s):
    ''' A string that is the same forward and backward
    is considered a palindrome
    Ex: "racecar", "hannah", "civic"'''
    if len(s) == 0 or len(s) == 1: # base case
        return True

    if s[0] != s[-1]:
        return False
    else:
        return isPalindrome(s[1:len(s)-1]) # continue checking

assert isPalindrome("racecar") == True
assert isPalindrome("civic") == True
assert isPalindrome("CS8") == False

# Example: Filter through and return a collection
def removeEvenNumbers(L):
    ''' For a list of numbers, L, returns a list where
    all even numbers are removed '''
    if len(L) == 0: # base case
        return []

    if L[0] % 2 == 0:
        return removeEvenNumbers(L[1:]) # discard item
    else:
        return [L[0]] + removeEvenNumbers(L[1:]) # keep item

assert removeEvenNumbers([1,2,3,4]) == [1,3]
assert removeEvenNumbers([1,1,1,1]) == [1,1,1,1]
assert removeEvenNumbers([2,4,6]) == []

# Example: Fibonacci
# A fibonacci sequence, the nth number in the sequence is the
# sum of the previous two. For example:
# f(n) = f(n-1) + f(n-2)
# f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, f(4) = 3, f(5)=5, ...

def fibonacci(n):
    if n == 1:      # base cases
        return 1
    if n == 0:
        return  0

    return fibonacci(n-1) + fibonacci(n-2)

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8

# Example: reverse a string
def reverseString(s):
    if s == "":     # base case
        return ""

    return reverseString(s[1:]) + s[0]


assert reverseString("CS8") == "8SC"
assert reverseString("") == ""
assert reverseString("a") == "a"
assert reverseString("hooray!") == "!yarooh"
```

