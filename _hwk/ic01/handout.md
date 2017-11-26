---
num: "ic00"
desc: "Code Review Exercise Handout"
ready: false
assigned: 2016-10-27 16:00:00.00-7:00
due: 2016-10-27 16:50:00.00-8:00
layout: handout
---

# {{site.qtr}}, {{page.num}}

## {{page.desc}}

(Note: Due date/time is one hour later for folks in 5pm section, and two hours later for folks in 6pm section.)

# Instructions: PART ONE (individual)

## Background

In [lab02](/labs/lab02/), you implemented:

```java
  public class Polynomial extends ArrayList<Integer>
```
One of the methods was the `toString()` method.   

Today, you will each be given two implementations of the `toString()` method by students from previous offerings of CS56.  
These students gave their permission for me to share these (anonymously) for this exercise.      
So the excerpts are identified by letter only: A, B, C, etc.

You need two different lettered copies, e.g. (A,B), (C,F), (D,K), etc.    
It does not matter which ones, as long as they are different—they don’t have to be consecutive.   You'll be in a group with other people
with whom you have at least one version in common.

## What you need to do:

You job is to review each of these.  Your job is not to tear apart the code, but to invite the author into a conversation.

* Please try to find at least two instances of good practice the author used. 
    * Identify these with a `+` sign, the line number(s), and a comment expressing approval of what they did well. 
* Please try to find at least two places where you think the code could be improved. (?)
    * Identify these with a `?` sign, the line number(s), and your concern *in the form of a diplomatic question*,
      rather than as a blunt statement.  
* Then find as many additional items as you can, of either type.


For example: 

```
Review of Solution "G":
+ 105,108,130   Clear use of comments to indicate purpose of code that follows
?  134 		    Would “power” be a better variable name than “x”?
etc.
```

Further instructions:

* Your two individual reviews go on the front side of the IC00 worksheet.
* When commenting on places where the code could be improved, you may like to phrase your remarks as a question that invites discussion, rather than as a direct critique.
* When offering comments, please be as specific as you can about how the effect of the good practice you are observing or suggesting.
* Find as many issues as you can, of both types (+ and ?). You should do your best to find at least two of each type, but don’t stop there

# SEE REVERSE SIDE FOR GROUP INSTRUCTIONS

<div style="page-break-before:always;">&nbsp;

</div>

# {{site.qtr}}, {{page.num}}

## {{page.desc}}

# Instructions—Part Two (group)


Now get into groups of four, based on ONE of the two codes you reviewed.   For example:

* one group should be four people that reviewed A
* another should be four people that reviewed B
etc.

You are now invited into a conversation with one another, where you produce a combined review.    You will take on four roles:

* Moderator—chairs the group and keeps meeting on track
* Reader—Reads out lines of code to be reviewed, one at a time. (skip initial javadoc)
* Recorder—Records what the group decides to mark down as issues
* Author—Advocates on behalf of the code

In fact, none of you is the author of the code—but one of you gets to pretend that she/he is.     This will help us practice being “diplomatic” in our sharing.  The “pretend author” should advocate for the code “as if” he/she authored it.

Note that ONLY THE RECORDER needs to write down what the group decides; this is a collective submission on behalf of the group, but you are ALL CO-REPSONSIBLE for that submission.    

# What to do:

```
foreach (line of code that isn’t initial javadoc) do {
	1) Reader reads the line of code
	2) Moderator asks group what issues they have
	3) All group members read their issues for this line  (moderator last)
	4) Moderator facilitates a discussion
	5) Recorder writes down the issues that reflect the group consensus
		(same syntax as for part 1)
        6) if (this is the last line of code)
	   do all steps 1-5 above again but 
	      from perspective of method “as a whole”
}
```

Moderator’s roles:

* Keep the discussion moving forward
* Encourage all members to participate
* Moderator may contribute their own ideas, but it is best to do so “last”
* Moderator should encourage forward momentum—try to avoid a situation where group gets “bogged down” on a particular point.   
* If group is having trouble reaching consensus on a particular line of code, consider summarizing both (or all three? four?) points of view, and moving on.

You only need one submission for each group of three-four people, but you are ALL COLLECTIVELY RESPONSIBLE for making sure that the
group submission has all of your names, and that it is filled out correctly.

You will be graded on:

* Using the correct format (see the syntax on the other side.)
* accuracy/reasonableness of critique
* most especially: diplomacy of critical remarks. For full credit, these *must* be phrased as a diplomatic question, not a blunt statement.


