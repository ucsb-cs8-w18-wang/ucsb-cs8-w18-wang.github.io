# Student(s): (insert name here)
# Make sure to read the comments for each function.

import pytest
'''
  You will write your own test cases (3 - 5 tests per function). 
  There's an example for each function to test: 
'''
####################
from lab08 import recursiveDigitSum

def test_recursiveDigitSum_0():
    assert recursiveDigitSum(9999) == 36

# Your tests for recursiveDigitSum...

####################
from lab08 import recursiveSubstring

def test_recursiveSubstring_0():
    assert recursiveSubstring("CS8", "CS") == True

# Your tests for recursiveDigitSum...

####################
from lab08 import recursiveReverseList

def test_recursiveReverseList_0():
    assert recursiveReverseList([1,2,3]) == [3,2,1]

# Your tests for recursiveReverseList...

####################
from lab08 import recursiveAccumulateVowels

def test_recursiveAccumulateVowels_0():
    assert recursiveAccumulateVowels("apple") == "ae"

# Your tests for recursiveAccumulateVowels...

