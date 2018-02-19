---
layout: lab
num: lab05
ready: true
desc: "2D Lists and Nested for Loops"
assigned: 2018-02-21 8:00:00.00-7
due: 2018-02-25 23:59:59.59-7
---

In this lab, you'll get more practice with:

* Writing functions
* Testing your functions with pytest
* Using nested for loops
* Iterating and modifying 2D lists

## This lab may be done solo, or in pairs.

Before you begin working on the lab, please decide if you will work solo or with a partner.

A reminder about working with a pair programming partner:

* Your partner must be enrolled in the same lab section as you.
* You and your partner must agree to work together outside of lab section in case you do not finish the lab during your lab time. You must agree to reserve at least two hours outside of lab section to work together if needed (preferrably during an open lab hour where you can work in Phelps 3525 and ask a mentor for help). You are responsible for exchanging contact information in case you need to reach your partner.
* If you choose to work with a partner, then you must choose a partner you have not worked with before.
* You MUST add your partner on Gradescope when submitting your work <strong>*<u>EACH TIME</u>*</strong> you submit a file(s). After uploading your file(s) on Gradescope, there is a "Group Members" link at the bottom (or "Add Group Member" under "Groups") where you can select the partner you are working with. Whoever uploaded the submission must make sure your partner is part of your Group. Click on "Group Members" -> "Add Member" and select your partner from the list.

Once you and your partner are in agreement, choose an initial driver and navigator, and have the driver log into their account.

# Instructions

In this lab, you will need to create two files:
* `{{page.num}}.py` - file containing function definitions
* `{{page.num}}_tests.py` - file containing test cases
* <strong>Please comment you and your partner's name (if applicable) at the top of each file.</strong>

Starter code is provided for you and are located at (you may need to refresh the page if the links do not load immediately):
* <https://ucsb-cs8-w18-wang.github.io/lab/lab05/lab05.py>
* <https://ucsb-cs8-w18-wang.github.io/lab/lab05/lab05_tests.py>

You will complete the portions in the starter code by doing the following:

1.  Create a directory called ~/cs8/{{page.num}} (using the `mkdir` command) and `cd` into that directory.
2.  Use `idle3` (you might try `idle3 &` if you want to be able to type commands on your terminal window after IDLE opens).
3.  Use "New File" to create empty files called `{{page.num}}.py` and `{{page.num}}_tests.py` in that `~/cs8/{{page.num}}` directory.
4.	Have some paper and a pen/pencil handy. Visualizing the 2D list and screen can help formulate your algorithms before writing the actual code.
5.  ONE AT A TIME, copy the function definitions from the starter code, and the tests that go along with those functions, and get the tests to pass.
   * By one a a time, what I mean is, at your first step, copy ONLY the first function definition from the starter code `{{page.num}}.py` and copy only the import statements and test cases from `{{page.num}}_tests.py` that go with that function definition.
   * Then, before you move on to the next function definition and <em>its</em> tests, get all of the tests from the one you just copied to pass.
   * Then, and only then, copy the next function definition and its tests into your files.
   * Repeat this until you have ALL of the function definitions and their tests, and all of them pass.
   * Since this lab is dealing with 2D lists, it may be hard to *visualize* your functions' behavior while inspecting the 2D lists in its list-of-lists form. Consider debugging and verifying small cases by printing the 2D list and manually checking your functionality before running the pytests. You should write these tests in the `if __name__=="__main__":` condition in `{{page.num}}.py` file. This code will not be executed when importing `{{page.num}}.py` into other python files.

You are encouraged to try submitting to Gradescope periodically for several reasons:

* You can get partial credit if some of your tests pass for some of your functions.
* You will have a backup of your file in case you accidentally delete yours, or in case your laptop dies.
* You can move code between your laptop and CSIL by downloading your submitted code from Gradescope

# A few notes about creating the screen

* Include the `create_screen` definition unmodified in your submission. Gradescope autograding requires this to be in your file and will not pass the tests if you forget to include this function in your `{{page.num}}.py` solution.
* `create_screen` will create a 2D list as discussed in lecture. This defines a screen of `row` x `column` "pixels".
	* `screen = create_screen(10,20)` will create a 10 x 20 pixel screen and assigns this 2D list to the variable `screen`. In this case, the rows are indexed [0-9] and the columns are indexed by [0-19].
	* For the functions you will need to implement, you may assume that the row and column values passed into the functions are correct types (integer) and within the screen dimensions (no need to do extra testing to account for this).
	* When printing the screen using `print_screen(screen)`, it will look like:

```
********************
********************
********************
********************
********************
********************
********************
********************
********************
********************
```

# A few notes about the `fill_rect` and `draw_rect` functions

* `fill_rect` will draw the area of a rectangle defined by the upper-left and lower-right points. For example, the `fill_rect(1,1,8,15,create_screen(10,20))` will update the screen as:

```
********************
*               ****
*               ****
*               ****
*               ****
*               ****
*               ****
*               ****
*               ****
********************
```

* `draw_rect` will draw the <strong>outline</strong> of a rectangle defined by the upper-left and lower-right points. For example, the `draw_rect(1,1,8,15,create_screen(10,20))` will update the screen as:

```
********************
*               ****
* ************* ****
* ************* ****
* ************* ****
* ************* ****
* ************* ****
* ************* ****
*               ****
********************
```

* For both `fill_rect` and `draw_rect`, if the upper-left point has the same row dimension as the lower-right point, then a simple line should exist. For example, the `fill_rect(1,1,1,15,create_screen(10,20))` or `draw_rect(1,1,1,15,create_screen(10,20))` statements will update the screen as:

```
********************
*               ****
********************
********************
********************
********************
********************
********************
********************
********************
```
* Similarly, for both `fill_rect` and `draw_rect`, if the upper-left point has the same column dimension as the lower-right point, then a simple line should exist. For example, the `fill_rect(1,1,8,1,create_screen(10,20))` or `draw_rect(1,1,8,1,create_screen(10,20))` statements will update the screen as:

```
********************
* ******************
* ******************
* ******************
* ******************
* ******************
* ******************
* ******************
* ******************
********************
```

# A few notes about the `draw_line` function

* This screen of pixels represented as a 2D list is not like a traditional cartesian coordinate system.
	* However, the point-slope equation still applies.
* The `draw_line` function's parameter has the `row1`, `col1` value of one pixel on the screen and `row2` and `col2` value of the other pixel on the screen.
	* Recall, the point-slope equation $$ y - y1 = m(x - x1) $$, where $$m$$ is the slope of the line between two points.
		* This can be applied to our screen representation where $$ m = (col1 - col2)/(row1 - row2) $$.
		* We can translate this into our scenario by thinking of this as $$ col - col1 = m(row - row1) $$.
			* We can then compute a specific `row` or `col` value for a pixel on the line.
		* Your code can check the valid rows and columns between two pixels and determine which pixel value on the line needs to be updated.
	* *Note1*: the resulting row and col values may be floating point numbers, but we cannot have indices of 2D lists be fractional values. In these cases, you will need to round these values using python's `round()` function, which returns a rounded int value.
	* *Note2*: your code should check the case if the `row1 == row2` since you will get an error by trying to compute the slope with $$(col1 - col2)/(row1 - row2)$$ 
	* *Note3*: you may also find the `min()` and `max()` python functions helpful when iterating through the range of rows and columns to check between the two pixels.
	* I suggest trying to work it out on paper first - it can help to visualize your algorithm first before translating this into code.

* An example of calling `draw_line(0,0,9,19,create_screen(10,20))` will update the screen as follows:

```
  ******************
**  ****************
****  **************
******  ************
********  **********
**********  ********
************  ******
**************  ****
****************  **
******************  

```
* and another example of calling `draw_line(1,28,5,1,create_screen(10,30))` will update the screen as follows:

```
******************************
*************************    *
******************       *****
************      ************
*****       ******************
*    *************************
******************************
******************************
******************************
******************************
```
* If both pixels are the same, then the single pixel will be drawn. An example of this is `draw_line(1,1,1,1,create_screen(10,20))` will update the screen as follows:

```
********************
* ******************
********************
********************
********************
********************
********************
********************
********************
********************
```

# Upload `{{page.num}}.py` and `{{page.num}}_tests.py` to Gradescope.

Once you're done with writing your functions, navigate to the Lab assignment "Lab05" on Gradescope and upload your `{{page.num}}.py` and `{{page.num}}_tests.py` files. <strong>*Remember to add your partner to Groups Members for this submission on Gradescope if applicable. At this point, if you worked in a pair, it is a good idea for both partners to log into Gradescope and see if you can see the uploaded files for Lab05.*</strong>


