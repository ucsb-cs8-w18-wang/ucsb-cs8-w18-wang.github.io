---
layout: lab
num: lab07
ready: true
desc: "Scrabble word finder: Python lists, dictionaries and file I/O"
assigned: 2018-03-07 8:00:00.00-7
due: 2018-03-11 23:59:59.59-7
---

In this lab, you'll get more practice with:

* using Python lists
* using Python dictionaries
* read data (words) from a text file and put them into a list
* create a Scrabble word finder
* use list method sort() to sort words in order of descending point value
* write formatted output to the screen and a file

## This lab may be done solo, or in pairs.

Before you begin working on the lab, please decide if you will work solo or with a partner.

A reminder about working with a pair programming partner:

* Your partner must be enrolled in the same lab section as you.
* You and your partner must agree to work together outside of lab section in case you do not finish the lab during your lab time. You must agree to reserve at least two hours outside of lab section to work together if needed (preferably during an open lab hour where you can work in Phelps 3525 and ask a mentor for help). You are responsible for exchanging contact information in case you need to reach your partner.
* If you choose to work with a partner, then you must choose a partner you have not worked with before.
* You MUST add your partner on Gradescope when submitting your work <strong>*<u>EACH TIME</u>*</strong> you submit a file(s). After uploading your file(s) on Gradescope, there is a "Group Members" link at the bottom (or "Add Group Member" under "Groups") where you can select the partner you are working with. Whoever uploaded the submission must make sure your partner is part of your Group. Click on "Group Members" -> "Add Member" and select your partner from the list.

Once you and your partner are in agreement, choose an initial driver and navigator, and have the driver log into their account.

## Getting started

* Step 1: Log on and open up a terminal window
This is done following the steps you have performed in lab00.
* Step 2: Create a directory in your cs8 directory named {{page.num}}.
* Step 3: Start IDLE

The terminal command for this is "`idle3 &`".  When you have the IDLE window up, you are ready for some programming!

## What to program?

In this lab assignment, you are going to make your own Scrabble word finder function, `scrabbleWords()`.  In the end, you will simply input a string of letters and the program will print out (to the screen and to a file) a list of all the possible words you can make along with their point values in descending order (neglecting things like triple letter, double word squares, etc. in the real game of Scrabble).  For example, if I input `'bouni'` as my string of letters, this is what I get:

```
>>> scrabbleWords('buoni')
obi      5
nub      5
nob      5
nib      5
bun      5
bio      5
bin      5
bi       4
uni      3
ion      3
on       2
nu       2
no       2
in       2
u        1
i        1
```

So, how did our program know which letter combinations were valid words?......We have to specify a file of words, which you can find here: [wordlist.txt](https://ucsb-cs8-w18-wang.github.io/lab/lab07/wordlist.txt).  This file must be downloaded (right click and "save as") and put into your `{{page.num}}` directory before you begin, so do that now.  Note that this file contains a fairly complete list of English words, so beware that there may be some expletive and/or raunchy words - please don't hold me personally responsible if you are offended.  Perhaps this will be motivation for some of you to complete the assignment.  

You can choose to start from scratch or use the starter code we have provided here (you may need to refresh the page if the links do not load immediately):
* <https://ucsb-cs8-w18-wang.github.io/lab/lab07/lab07.py>
* <https://ucsb-cs8-w18-wang.github.io/lab/lab07/lab07_student_tests.py>

### Functions to Implement:

1. **createWordList(filename)** - return a list of strings
2. **canWeMakeIt(myWord, myLetters)** - return True or False
3. **getWordPoints(myWord, letterPoints)** - return an integer representing the point value for a word
4. **outputWordPointPairs(pointWordList, myLetters, toFile)** - NO return (just prints a formatted list or writes it to a file).
5. **scrabbleWords(myLetters)** - NO return (just calls other functions)

### Function Details:

1. **createWordList(filename)** - return a list of strings.  Write a function which reads the file `filename` and returns a list containing all the words in the file.  Note that the last character of every line of the file is the invisible "new line" character `'\n'` and needs to be sliced off.

2. **canWeMakeIt(myWord, myLetters)** - return True or False.  Write a function which answers the question: Can I form the word `myWord` from the string of letters `myLetters`?  The function should return a boolean True or False.  Converting `myLetters` to a list and using the pop() or remove() method may come in handy. You do not need to use all the letters in `myLetters`. It's possible that `myLetters` will contain multiples of the same letters. In the example above if `myLetters = "buoni"`  and `myWord = "boon"` it should return False. If the input is not the correct type then return `False` Try to write an algorithm on paper first before attempting to write the code. Think about the list functions at your disposal and the tools you've learned up till now.

3. **getWordPoints(myWord, letterPoints)** - return an int representing the points for myWord.  Write a function that calculates and returns the total point value of `myWord` given the Python dictionary object `letterPoints` which consists of letter:pointValue pairs. If a character in `myWord` is not a key in the provided dictionary then its score value is 0. If any of the input is incorrect type then return 0. Note that you do not need to create the `letterPoints` dictionary in this step - it is a parameter to our function and will be created in `scrabbleWords()`.

4. **outputWordPointPairs(pointWordList, myLetters, toFile)** - NO return (just prints a formatted list or writes it to file).

* Write a function which will output the (pointValue, word) pairs in pointWordList to the shell or to a file depending on the bool value `toFile`

* When `toFile` is `False`,  print all the words followed by their point value.  Format the output so that your word is left justified in a field of width 4 more than the number of letters in `myLetters`, and the point value follows immediately afterwards.  You can do this with the format string method by carefully forming the `'{...}'` string first.

* If `toFile` is `True`, write the same text as your formatted screen output from above to a text file.  Name the file the string of letters contained in `myLetters` followed by .txt.  So in the example above with scrabbleWords("buoni"), the file that is created is `buoni.txt`.  Note that every time you want to write to a new line, you will need to include the newline character '\n' in your file.write() statement.  You can see what the output should look like in the example here: [buoni.txt](https://ucsb-cs8-w18-wang.github.io/lab/lab07/buoni.txt). You can simply verify that when you run your program you produce this same file if `myletters` == `"buoni"`.

### Putting it all together:

**scrabbleWords(myLetters)** - NO return (just calls the helper functions above).  Here you will call upon your "helper functions" created in steps 1-4 to form a list of all the words (from wordlist.txt) that can be formed from the set of letters contained in myLetters:

* Create a Python list of strings containing the words from `wordlist.txt`.  You will want to call helper function `createWordList()`.

* Create a list of all the words that we can make with `myLetters` by looping through every word in `wordList` and checking if it can be made with `myLetters`.  You will want to call helper function `canWeMakeIt()`.

* Create a dictionary of letter: pointValue pairs - name it `letterPoints`.  The image below shows the Scrabble point value for each letter, but note that your dictionary keys should be the lower case letters. Any character that is not shown in this image has a point value of 0. You don't have to add 0 point keys to your dictionary, rather make sure that your `getWordPoints` uses a point value of 0 if a letter is not in the provided dictionary.

![letter points](scrabble_letters.png){:height="200px"}

* Create a list of tuples consisting of (pointValue, word) pairs by looping through the list `myWords` and getting the point value for each word - name this list of tuples `pointWordList`.  To calculate pointValue, you will want to call helper function `getWordPoints()`.

* Sort `pointWordList` in descending order.  Now, you can use the list method sort() to sort the tuples according to their first entry, pointValue.  But sort() arranges a list in ascending order by default....can you think of a way to reverse this?

* Call your `outputWordPointPairs()` and print your formatted string output to terminal. Then make a second call to `outputWordPointPairs()` to output to a .txt file named after the string in `myLetters`.

## Write test code in {{page.num}}_student_tests.py

You must write your own tests using pytest for the following functions: 
* `createWordList(filename)`
* `canWeMakeIt(myWord, myLetters)`
* `getWordPoints(myWord, letterPoints)`

Write the test code before you implement the functions. This is a way of demonstrating that you understand what each function is supposed to do.

You should test the other two functions manually, although you are welcome to write test code for them as well.

Put your test code in `{{page.num}}_student_test.py` and submit it along with your `{{page.num}}.py` file.
This test code is worth some amount of points for this lab. We recommend writing at least 3-5 test cases per function, but feel free to write more until you're confident with your solution.

Note that Gradescope will only give you a partial score. Gradescope will use test cases different from the tests that you will wrote in `{{page.num}}_student_test.py`.

### What {{page.num}}.py should look like

```
import pytest
#other import statements"

def createWordList(filename):
  #Your code

def canWeMakeIt(myWord, myLetters):
  #Your code

def getWordPoints(myWord, letterPoints):  
  #Your code

def outputWordPointPairs(pointWordList, myLetters, toFile):
  #Your code

def scrabbleWords(myLetters):
  #Your code

if __name__=="__main__":
  print("Manual test cases can be done here and/or in IDLE's command line")
  # manual tests

```
### What {{page.num}}_student_tests.py should look like

```
import pytest
from {{page.num}} import createWordList

def test_createWordList_0():
  #Your test code


def test_createWordList_1():
  #Your test code
....


from {{page.num}} import canWeMakeIt

def test_canWeMakeIt_0():
  assert(canWeMakeIt('ape','pae') == True)

...
from {{page.num}} import getWordPoints
letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4,\
                'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1,\
                'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,\
                's':1, 't':1, 'u':1, 'v':4,  'w':4, 'x':8,\
                'y':4, 'z':10}

def test_getWordPoints_0():
  assert(getWordPoints('ape',letterPoints) == 5)
...
```


# Running the final product

You can load your `{{page.num}}.py` and run `scrabbleWords` in IDLE's interactive shell. In `scrabbleWords` you <strong>must</strong> make one call to print to the console with `outputWordPointPairs` where `toFile = True`, and another call to write to a file with `outputWordPointPairs` where `toFile = False`. Gradescope test cases will fail if you forget to write your output to a file.

# Upload `{{page.num}}.py` and `{{page.num}}_tests.py` to Gradescope.

Once you're done with writing your functions, navigate to the Lab assignment "{{page.num}}" on Gradescope and upload your `{{page.num}}.py` and `{{page.num}}_student_tests.py` files. <strong>*Remember to add your partner to Groups Members for this submission on Gradescope if applicable. At this point, if you worked in a pair, it is a good idea for both partners to log into Gradescope and see if you can see the uploaded files for {{page.num}}.*</strong>

Thanks to Matt Buoni for this lab!
