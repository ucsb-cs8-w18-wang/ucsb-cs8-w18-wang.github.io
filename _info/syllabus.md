---
title: "Syllabus, CMPSC 8, Winter 2018"
layout: handout
ready: false
---

Basic Facts
-----------

* **Course Web Site**: <http://ucsb-cs8.github.io>
* **Instructor**:  [Richert Wang](http://www.cs.ucsb.edu/~richert)
   * Email is richert@ucsb.edu, BUT please use [Piazza](https://piazza.com/class/jc6t3qhjbc2pb) for course related communication.
* **Lecture**: TuTh 2:30pm-3:45pm BUCHN1920, ATTENDANCE REQUIRED.
* **TAs**:  {{site.ta_list_full}} (contact via Piazza.com)
* **Lab** (50 minute discussion section) Wednesdays 10am, 11am , 12pm - Phelps 3525, ATTENDANCE REQUIRED.                                         
* Office Hours: Tuesday 3:30pm - 4:30pm, Thursday 12pm - 1pm in HFH 1151

# Required Resources

* Textbook: "Introduction to Computing Using Python" - Ljubomir Perkovic, 2nd edition

Official UCSB Catalog Description
---------------------------------

<div style="background-color:#eee; border: 8px inset #333; font-size:90%; margin:1em; width:45em; padding: 0.5em;" markdown="1">

CMPSC 8: Introduction to Computer Science

Not open for credit to students who have completed Computer Science 16 or Engineering 3.

Introduction to computer program development for students with little to no programming experience. Basic programming concepts, variables and expressions, data and control structures, algorithms, debugging, program design, and documentation.

</div>

## A few course policies in brief

* If you are registered for another UCSB course that overlaps with this one, you MUST HAVE specific written permission from both instructors, or I am within my rights to give you a failing grade on any work you miss as a result, and will NOT make any accommodations for you. This includes exams.
* Collaboration is only permitted when specifically allowed for—otherwise, you must do your own work.
   * On most homework assignments you may collaborate with at most one other person (who must be named).
* Attendance is required at all lectures and labs (discussion sections).
  * I recognize that some absences (e.g. minor illnesses, mishaps, etc.) are unavoidable. Litigating whether each of these is "excused" or not isn't a good use of anyone's time, so instead we will drop the lowest two grades from everyone's homework. This way, absenses (or failure to submit homework) does not unduly penalize your grade unless it becomes excessive.
* <strong>You</strong> must turn in your homework in lecture the day that it is due.
* We will use the gradescope system (https://gradescope.com) this quarter. More instructions on gradescope will be given in lecture and lab assignments.
* Any regrade requests must be made on Gradescope and we will not consider a regrade request one week after the assignment grades are distributed back to students.

You may NOT: 

* Turn in homework on a day other than when it is due (early or late)
* Have someone else turn in your homework for you (that will be considered academic dishonesty).
* Drop it off with the instructor or TA to be graded later.

## What this course is about 

This class serves as an <strong>introduction to programming and computer science</strong>. We will use the Python language and write Python programs throughout the course. We will be using Python 3 in the class. The Python Interpreter can be downloaded for free from Python's download page (http://python.org/downloads/). I encourage everyone to install Python on their local computer in order to practice programming in your own time.

If you find yourself working on a computer that doesn't have Python installed, you can run simple Python code (along with several other languages) on the web (https://ideone.com). This is not a requirement for the course, but you may find it to be a useful tool.

Learning how to program requires <strong>A LOT</strong> of practice like learning any new skill. Making mistakes is an essential part of learning as long as you learn from them! Questions like "I wonder what will happen if I do this..." or "How will Python behave in this case..." is a great way to investigate and observe the functionality and limitations of a programming language (there are many programming available to software developers and each have their specific pros and cons that may be the best choice for the problems you are trying to solve).

I find the best way to practice is to <strong>rapid prototype</strong> constantly. Writing simple snippets of code to test and confirm your understanding allows you to 1) practice typing out code, which makes you more comfortable with the language and 2) understanding the specific behavior of the programming language functionality.

Programming is the study of <strong>algorithms</strong>, i.e. step-by-step instructions telling the computer what it needs to do. There are <strong>MANY</strong> algorithms that can solve a problem and it's important to consider the computational time, memory space, and correctness of the algorithms you create.

## Why Python?

* Python is a popular choice for introductory programming courses since it is easier to learn than C/C++ and Java.
* Python is a largely supported language and is widely used in academia and industry. There is a large support for Python that comes with the language itself and 3rd party libraries you can use for many types of applications.

# What you need to learn to become a skilled beginning level programmer

So, what is it that you need to know to be a skilled beginning-level programmer in Python? Here's the  list of what you'll need to be ready for CMPSC&nbsp;16 (aka CS16, the next programming course):

<table border="1" cellspacing="1" cellpadding="1" id="topicTable">
  <tr>
    <td><ul class="style11">
      <li>Problem solving
        <ul>
            <li>breaking down a problem into a sequence of steps</li>
          <li>abstracting specific problems into general ones<br />
            and finding general solutions</li>
        </ul>
      </li>
      <li>Memory concepts
        <ul>
            <li>variables, primitive vs. reference variables, name, type, value</li>
          <li>assignment statements</li>
          <li>scope of variables</li>
        </ul>
      </li>
      <li>Control structures
        <ul>
            <li>for loops, if/else, while loops</li>
        </ul>
      </li>
      <li>Lists in Python (similar to arrays in other languages)
        <ul>
            <li>index vs. value, finding sum, min, max, average, count of elements matching some condition, making a new list of elements containing only those that match some condition</li>
        </ul>
      </li>
    </ul>    </td>
    <td><ul class="style11">
      <li>Functions
        <ul>
            <li>function call vs. function definition</li>
          <li>formal vs. actual parameters (arguments)</li>
        </ul>
      </li>
      <li>Testing
        <ul>
            <li>How to test your code</li>
        </ul>
      </li>
      <li>Input/output concepts
        <ul>
            <li>Writing to the terminal</li>
          <li>Reading from the keyboard</li>
          <li>Reading and writing to files</li>
          <li>Neatly formatting output</li>
        </ul>
      </li>
      <li>Program style
        <ul>
            <li>How to write code that other people can read and understand</li>
        </ul>
      </li>
    </ul>    </td>
  </tr>
</table>

## Course Grades

Letter grades will be determined by the end of the course after all labs, homeworks, and exams have been computer. I can say that I will not grade harder than a traditional straight scale (90% = A-, 80% = B-, etc.). However, I will adjust the letter grades accordingly based on your overall performance at the end of the course. If you are concerned about your grade in the class, I encourage you to discuss the matter with me during my office hours. Please come talk to me sooner rather than later so there will be some time where we can help you succeed in the course.

Your course grade will be determined as follows:

| Grade Item                                                              | Percentage of Final Grade |
|-------------------------------------------------------------------------|---------------------------|
| Midterm 1                                                               | 15 %                      |
| Midterm 2                                                               | 15 %                      | 
| Final                                                                   | 30 %                      |
| Hwks                                                                    | 10 %                      |
| Labs                                                                    | 30 %                      | 

<div style="page-break-before:always;">
&nbsp;
</div>

## Late work

I will consider late submissions <strong>only</strong> for medical or family emergencies where documentation can be provided. This does not include overwhelming workload from other courses, scheduling conflicts, or vacation plans.

* There will not be any make ups for examinations.
* Two of the lowest homework scores will be dropped. Late homework submissions will not be accepted. However, even if you know you will not be able to submit a homework, I highly encourage you to complete it anyways since the homeworks will help prepare you for the examinations.
* All labs must be submitted by the due date. Depending on the case, your TA may consider grading your lab with a late penalty (and usually for cases where the submission was done very soon after the deadline). However, this is not an official policy and you risk receiving a zero for a late lab submission. 


Accommodations for disabilities
-------------------------------

Students with disabilities may request academic accommodations for exams online through the UCSB Disabled Students Program at http://dsp.sa.ucsb.edu/. Please make your requests for exam accommodations through the online system as early in the quarter as possible to ensure proper arrangement.

Managing stress
---------------

Personal concerns such as stress, anxiety, relationships, depression, cultural differences, can interfere with the ability of students to succeed and thrive. For helpful resources, please contact UCSB Counseling & Psychological Services (CAPS) at 805-893-4411 or visit http://counseling.sa.ucsb.edu/ .

Responsible scholarship
-----------------------

Honesty and integrity in all academic work is essential for a valuable educational experience.  The Office of Judicial Affairs has policies, tips, and resources for proper citation use, recognizing actions considered to be cheating or other forms of academic theft, and students’ responsibilities, available on their website at: http://judicialaffairs.sa.ucsb.edu.  Students are responsible for educating themselves on the policies and to abide by them.

Furthermore, for general academic support, students are encouraged to visit Campus Learning Assistance Services (CLAS) early and often. CLAS offers instructional groups, drop-in tutoring, writing and ESL services, skills workshops and one-on-one consultations. CLAS is located on the third floor of the Student Resource Building, or visit http://clas.sa.ucsb.edu

Standard Disclaimer
-------------------

This syllabus is as accurate as possible, but is subject to change at
the instructor's discretion, within the bounds of UC policy.

(end of syllabus)

</div>
