---
title: "Syllabus, CMPSC 56, Fall 2017"
layout: handout
ready: false
---

<div style="font-size:110%;" markdown="1">

Basic Facts
-----------

* **Instructor**:  [Phill Conrad](http://www.cs.ucsb.edu/~pconrad)
* **Lecture**: TR 09:30pm-10:45pm BUCHN 1930, ATTENDANCE REQUIRED.
* **TAs**: {{site.ta_list_full}} (contact via Piazza)
* **Lab** (50 minute discussion section) Thursday {{site.discussion_section_times}}, Phelps 3525, ATTENDANCE REQUIRED.                                         
* Office Hours: See: <http://www.cs.ucsb.edu/~pconrad/ofchrs>  

For course website links, visit the course Gauchospace site.

About the Course
----------------

-   Our goal is to learn Java---but not just to learn Java for the sake of learning Java. After all, some of you already "know Java", at some level.
-   Our bigger goals are:
    -   to practice using big APIs to get stuff done--a very relevant real world job skill!
    -   to learn how to learn a new language or technology--something you'll do a lot in your career
    -   to learn about a few specific topics: the JVM, threads, Swing GUIs, etc..
    -   to learn some professional-level, real-world programming practices.

The way I'm planning to teach the course is a bit different from what you may have experienced before--I'm trying to create a learning environment that *mirrors how real world software is developed* more than is the case is traditionally structured courses.

So, the emphasis will be on:

-   open source, and sharing code, not keeping code secret
-   collaboration
-   writing code, that, where possible is actually useful and usable.

Note that "sharing code" doesn't mean "stealing code". We still don't take credit for other people's work---academic honesty still applies. It just 'looks different' in this course.

The official course description is here:

<div style="background-color:#eee; border: 8px inset #333; font-size:90%; margin:1em; width:50em; padding: 0.5em;" markdown="1">

CMPSC 56. Advanced Applications Programming
(4) STAFF
Prerequisite: Computer Science 24 and 32 with a grade of C or better

Advanced application programming using a high-level, virtual-machine-based language. Topics include generic programming, exception handling, programming language implementation; automatic memory management, and application development, management, and maintenance tools; event handling, concurrency and threading, and advanced library use.

</div>

<div style="page-break-before: always; font-size:100%;" markdown="1">

Final Course Grades
===================

The formula to determine your course grade average is explained in the table below.

Regardless of any other policies spelled out here, the average used to determine your final letter grade may be no higher than one full letter grade higher than your exam average.

Thus,

-   reasonably good performance on exams is very important to earning a good final grade in the course.
-   an A or B should not be out of reach for anyone that has a reasonably good mastery of course concepts (enough to earn a B or C on the exams), and puts in hard work on the labs and project points.

To convert final averages to letter grades, a standard 10 point scale will be used, with the upper and lower ends of each range as +/- grades, except
for A+ grades, see below.  There is no "rounding up"; a grade of 86.9999 is a B and a grade of 87.0000 is a B+.

A+ grades: These may be awarded to the very best performing students in the class—but the cutoff for A+ grades will be determined at the end of the course at the discretion of the instructor (there is no pre-determined cutoff---an average of 97 or more doesn't guarantee you an A+ grade.)

| Grade Item                                                                   | Percentage of Final Grade |
|------------------------------------------------------------------------------|---------------------------|
| Midterm 1 | 20 % |
| Midterm 2 | 20 % |
| Final | 20 % |
| Hwks, In Class Assignments | 10 % |
| Labs (typically closed source, some open source) | 10 % |
| Projects (open source) | 20 % |

Missing homework/in-class activities: Drop the lowest 4
-------------------------------------------------------

If you miss a class, you miss the opportunity for the points on that
in-class assignment, or homework that was due. Period.

There is no makeup. In lieu of providing a makeup opportunity, I will
drop the lowest 4 homework/in-class-assignment grades (which may be
zeros if you miss an assignment.) Each homework and in-class-activity
will be of equal value (100 pts).


Notes sheets on exams
---------------------

-   You are permitted one 8.5 x 11 (standard US letter size paper) sheet of notes for each exam.
-   You are permitted only one sheet per exam.
-   Your notes sheet will be collected and WILL NOT BE RETURNED
-   So, if you need a copy of it, make a copy BEFORE you come to the exam.


More On Grading
---------------

We'll have three exams--two midterms and a final. That part of the course will be traditional. And, there will be some traditional lab and homework assignments (and perhaps quizzes) where "everybody in the class does roughly the same thing"---those make up another 20% of your grade.

Note that, at the discretion of the instructor, part of one of the midterms, and/or part of the final exam may a "lab final", i.e. a set of exercises done in the laboratory setting under exam conditions.   The division of points between written final the lab final will be at the discretion of the instructor, and announced later in the quarter.

The remaining part of your grade--the last 20%--comes from project points which are explained in more detail later in this syllabus.

</div>

<div style="page-break-before:always;">
&nbsp;
</div>

<div style="font-size: 120%;">

Project Points
==============

Project points assignments can be found in public github repositories in the Organization: <http://github.com/organizations/UCSB-CS56-Projects>. The way in which these will be assigned will be explained later in the course.

To earn a "perfect score" (100%) for this 20% component of your grade, you need to earn 1000 project points. If you only earn 800, then an 80% will be recorded for that 20% of your grade.

Some projects are worth more points, and some worth fewer.

If you accumulate more than 1000 project points, up to 100 project points may be used to raise your final average in the class up to 2.0 points. (The points will be recorded as extra credit). (Each point raises your final course average by 0.02% ).

You may not earn more than 1100 total project points--any points in excess of 1100 will not count towards your grade (though you'll probably learn a lot from having under taken the work to earn them.)

### Project Point Deadlines

-   You may earn up to 1100 project points over the course of the quarter
-   There may be intermediate deadlines by which you need to accmulate certain numbers of points, e.g. 500, 800, etc.
-   The final deadline for project points is the last day of instruction at 5pm.

How to interpret these "due dates":


-   Unless told otherwise in the instructions for a particular project points assignment, you may complete any project point assignment at any time.
-   However, the points have to be "recorded" somewhere to count towards your grade.
-   Before the first deadline , you have the possibility to earn up to 1100 project points.
-   If there is a deadline for the first 300 points (Project deadine 1), if you haven't yet completed/submitted any project points work, the maximum number you can earn is now 800 (1100-300).
-   If there is a second deadline for 300 more points (Project 2), if you haven't yet completed/submitted any project points work, the maximum number you can earn is now 1100-600= 500.
-   You may "work ahead"---that is, if you earn 800 points for your first assignment, we'll count 300 towards Project 1, 300 towards Project 2, and 200 towards Project 3.
-   However, once a deadline has passed, only project points earned before that deadline may be applied to that assignment.


</div>

<div style="page-break-before:always;">
&nbsp;
</div>

<div style="font-size: 120%;" markdown="1">

Late Labs
---------

The policy is simple, and is based on the idea that the primary
purpose of the deadlines is to allow the TA manage his/her
workload. The number of labs in this course requires that he/she not
have to do "context switching" between grading different labs. All
labs must be graded in one sitting, or he/she just won't be able to
keep up with the workload.

So:

-   If you want your work to be graded without penalty, turn it in on time.
-   If you turn in your lab late, you RISK GETTING A ZERO.
-   We will grade late labs ONLY if it creates no extra inconvenience for the graders, and we WILL impose a penalty between 10-20% (see the individual grading rubrics for the labs.)
-   There is NO GUARANTEE that late labs will be graded at all. The TA will simply start work at some point after the deadline, and grade until he/she is finished. At that time, he/she will "close the books" on that particular lab, and any work not submitted at that time will NOT be considered.


Attendance
==========

This course moves quickly. So attendance is very important.

We'll be trying to master the material from about 14 chapters in the
Head First Java book, and several chapters of the Head First Design Patterns book.   That's a pace of about 4 chapters per week. We need to go at that pace,
because we'll lose a couple of weeks to exams, and the last few
lectures the quarter, you can't really start anything new, because
there isn't time to put it into practice with programming
assignments.    If you don't put it into practice, you aren't very likely
to learn it in any way that is going to stick with you, so there isn't
much point in just "going through the motions".

As a result, there will be something you have to turn in at almost
every class, plus some times when you have to submit homeworks electronically
through Gradescope.   In this way, attendance is taken, and required.

These things you have to turn in will be a combination of in-class
activities, and homework completed outside of class, but handed in on
paper during class.

In class activities may occur at anytime, announced or unannounced. Missed
in-class activities  may not be made up, except by "dropping the lowest 4".

Thus attendance is required, and reading the assigned readings is
required.

</div>

<div style="page-break-before: always; font-size:120%;" markdown="1">

Questions about grades
----------------------

**Summary: regrade requests must be made only on GradeScope, and always within one week.**

From time to time, the people who grade your papers may make clerical
errors in grading (e.g. adding up points wrong or applying a rubric
incorrectly.) For this reason, you are encouraged to review your
grades as they are posted to Gradescope and Gauchospace. You will
typically get an email as soon as each grade is posted. From the time
the grade is posted, you will have one calendar week to post regrade
requests. These must be made ONLY through Gradescope, ON the correct
problem. (Don't request a regrade for question 4 on the page for
question 7.)

Please note that <b>regrade requests based on clerical errors or
applying a rubric incorrectly are always welcome</b>. Over the course
of the quarter, we'll grade over 10,000 individual problems, so it is
unlikely that we won't make at least some mistakes.

<b>More problematic are challenges to the rubric itself</b>, e.g. "I
don't think you should have taken off so many points for that error"
or "I think I deserve more partial credit for that incorrect
answer". The instructor and TA will always listen, but please know
that we've put a great deal of thought, time and experience into
determining the rubric, and we've done our best to apply it to all
students equitably. You may have a different point of view, we will
not always agree with your assessment—in fact, we seldom will. <b>As
such, regrade requests on this basis are not encouraged.</b> It is
important to approach such conversations in a respectful manner,
accepting that the instructor, TA and grader have been given
responsibility for determining course standards, and applying those in
a fair way to all students.

In any case, once the two week deadline for challenges has passed,
each grade becomes final---and it is your responsibility to come to
scheduled TA or instructor office hours to have this discussion. If
you cannot make office hours, you may request an appointment, but you
must request the appointment within ONE WEEK of the assignment being
posted. If you wait until the last office hours opportunity during the
two week window, and you are not able to be seen (e.g. because of a
long line of students), then you lose the right to appeal your grade.

</div>

<div style="page-break-before:always;">
&nbsp;
</div>

<div style="font-size: 120%;">


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
