# lab07_student_tests.py - Tests for CS8 lab07

import pytest
'''
  You should write your own test cases using pytest. 
  Here are some examples for each function to test: 
'''

from lab07 import createWordList

#### Write tests for createWordList ####

def test_createWordList_0():
  # Example test
  #Write to a file with words in it
  words = ['computer', 'science', 'python']
  outfile = open('test_file_0.txt', 'w')
  for item in words:
    outfile.write(item +'\n')

  outfile.close()

  # Read the file with words created in it to test if createWordList
  # creates a list of words correctly.
  newlist = createWordList('test_file_0.txt')
  assert(len(newlist) == len(words))
  
  for i in range(len(words)):
    assert(words[i] == newlist[i])


def test_createWordList_1():
  assert False

#...

from lab07 import canWeMakeIt

#### Write tests for canWeMakeIt ####

def test_canWeMakeIt_0():
  # Example Test
  assert(canWeMakeIt('ape','pae') == True)


def test_canWeMakeIt_1():
  assert False

#...

#### Write tests for getWordPoints ####

from lab07 import getWordPoints
letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,\
                'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,\
                'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
                's':1, 't':1, 'u':1, 'v':4,  'w':4, 'x':8,\
                'y':4, 'z':10}


def test_getWordPoints_0():
  # Example Test
  assert(getWordPoints('ape',letterPoints) == 5)


def test_getWordPoints_1():
  assert False

#...
