---
layout: lab
num: lab06
ready: true
desc: "String Formatting, Random, and File IO"
assigned: 2018-02-28 8:00:00.00-7
due: 2018-03-04 23:59:59.59-7
---

In this lab, you'll get more practice with:

* Using `randrange`
* Testing your functions with pytest
* Using String Formatting
* Reading and processing files

## This lab may be done solo, or in pairs.

Before you begin working on the lab, please decide if you will work solo or with a partner.

A reminder about working with a pair programming partner:

* Your partner must be enrolled in the same lab section as you.
* You and your partner must agree to work together outside of lab section in case you do not finish the lab during your lab time. You must agree to reserve at least two hours outside of lab section to work together if needed (preferably during an open lab hour where you can work in Phelps 3525 and ask a mentor for help). You are responsible for exchanging contact information in case you need to reach your partner.
* If you choose to work with a partner, then you must choose a partner you have not worked with before.
* You MUST add your partner on Gradescope when submitting your work <strong>*<u>EACH TIME</u>*</strong> you submit a file(s). After uploading your file(s) on Gradescope, there is a "Group Members" link at the bottom (or "Add Group Member" under "Groups") where you can select the partner you are working with. Whoever uploaded the submission must make sure your partner is part of your Group. Click on "Group Members" -> "Add Member" and select your partner from the list.

Once you and your partner are in agreement, choose an initial driver and navigator, and have the driver log into their account.

# Instructions

In this lab, you will need to create two files:
* `{{page.num}}.py` - file containing function definitions
* `{{page.num}}_tests.py` - file containing test cases
* <strong>Please comment your (and your partner's name (if applicable)) at the top of each file.</strong>

Starter code is provided for you and are located at (you may need to refresh the page if the links do not load immediately):
* <https://ucsb-cs8-w18-wang.github.io/lab/lab06/lab06.py>
* <https://ucsb-cs8-w18-wang.github.io/lab/lab06/lab06_tests.py>
* <https://ucsb-cs8-w18-wang.github.io/lab/lab06/input1.txt>
* <https://ucsb-cs8-w18-wang.github.io/lab/lab06/input2.txt>

1.  Create a directory called ~/cs8/{{page.num}} (using the `mkdir` command) and `cd` into that directory.
2.  Use `idle3` (you might try `idle3 &` if you want to be able to type commands on your terminal window after IDLE opens).
3.  Use "New File" to create empty files called `{{page.num}}.py` and `{{page.num}}_tests.py` in that `~/cs8/{{page.num}}` directory.
4.  Download `input1.txt` and `input2.txt` in that `~/cs8/{{page.num}}` directory. These are used when running pytest on {{page.num}}_tests.py.

You are encouraged to try submitting to Gradescope periodically for several reasons:

* You can get partial credit if some of your tests pass for some of your functions.
* You will have a backup of your file in case you accidentally delete yours, or in case your laptop dies.
* You can move code between your laptop and CSIL by downloading your submitted code from Gradescope.

# Some notes about printing the dice distribution

This portion of the lab will be manually graded by our TAs and not autograded by gradescope (though your submission must include the `rollDice`, `rollDistribution` and `printDistribution` functions in `{{page.num}}.py`.

An example `printDistribution` function will appear as follows:

```
Distribution of dice rolls

 2:     7 (  2.8%)  *******
 3:    14 (  5.6%)  **************
 4:    29 ( 11.6%)  *****************************
 5:    26 ( 10.4%)  **************************
 6:    34 ( 13.6%)  **********************************
 7:    41 ( 16.4%)  *****************************************
 8:    30 ( 12.0%)  ******************************
 9:    23 (  9.2%)  ***********************
10:    23 (  9.2%)  ***********************
11:    16 (  6.4%)  ****************
12:     7 (  2.8%)  *******
------------------------------
250 rolls
```

* The first line is simply "`Distribution of dice rolls`" followed by an empty line.
* The dice rolls are printed in a histogram format, one for each roll with additional information.
	* Your solution should print this portion while iterating through the diceTally in a loop using the `.format` function. <strong>Do not simply write 10 print statements using `.format`.</strong> 
	* The dice roll values will have two spaces right-justified followed by a `':'` character.
	* Six spaces are reserved to print number of times a particular roll occurred, which is right-justified, followed by an empty space and open parenthesis, `'('`, characters.
	* 5 spaces are reserved for the actual percentage value, with one space for the floating point value. This is followed by the `'%)'`, and two blank spaces.
	* The `'*'` character is printed the number of times a particular dice roll occurred.
* 30 hyphens `-` are printed after the diceRolls are printed
* The number of rolls are then printed.
* Using your function definitions, the following statement should display an output similar (but not exactly since `rollDice` is random) to the output shown above:

```>>> printDistribution(rollDistribution(250))```

# Some notes about the File I/O functions

This portion of the lab will be autograded by gradescope. Two input files are provided for you to test your functionality. One additional input file is not provided and will be tested with your submission on Gradescope.

Note that all words are separated by a whitespace character, and a word contains only alpha-numeric characters that does not include punctuation characters. For simplicity, you may assume the text only contains the `,.!?;` punctuation characters. Your code will need to split and strip the text file string appropriately.

# Upload `{{page.num}}.py` and `{{page.num}}_tests.py` to Gradescope.

Once you're done with writing your functions, navigate to the Lab assignment "Lab06" on Gradescope and upload your `{{page.num}}.py` and `{{page.num}}_tests.py` files. <strong>*Remember to add your partner to Groups Members for this submission on Gradescope if applicable. At this point, if you worked in a pair, it is a good idea for both partners to log into Gradescope and see if you can see the uploaded files for Lab06.*</strong>
