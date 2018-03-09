---
num: "Lecture 13"
desc: "More on Sets and Dictionaries"
ready: true
date: 2018-03-08 14:30:00.00-7:00
---

```
# CS 8, 3-8-18

''' Last time
- Introduced Dictionaries
- Introduced Sets
- Today: Continue with some set operations
- Talk about BENCHMARKING
'''

s2 = set([2,4,6])
s3 = set([4,5,6])

# Set comparisons
print(s2 == s2)             # True
print(s2 == s3)             # False
print(s2 != s3)             # True
print({1,2} < {1,2,3})      # True, < indicates "proper" subset
print({1,2,3} < {1,2,3})    # False
print({1,2} > {1})          # True
print({1,2,3} > {1,2})      # True
print({1,2,3} >= {1,2,3})   # True
print({1,2,3} >= {2})       # True , <= indicates a subset

print({1,2,4} == {2,1,4})   # True , order doesn't matter

# Set methods:
s2.add(100)
print(s2)
s2.add(100) # Doesn't add duplicates
print(s2)
s2.remove(2)
print(s2)
#s2.remove(10101) # ERROR, 10101 does not exist
s2.discard(10101) # same as remove, but doesn't crash if not there
s2.clear()
print(s2)

# Example - Performance in searching through lists vs dict.
# wordlist.txt (a list of words, one per line)
# PeterPan.txt (Peter Pan novel in a .txt file)

# Gutenberg.org - classic books in text!
# https://www.gutenberg.org/browse/scores/top
# Example using today is: Peter Pan
'''
DICT = {}
infile = open("wordlist.txt", 'r')
for x in infile:
    DICT[x.strip()] = 0
infile.close()

LIST = []
for y in DICT:
    LIST.append(y)

from time import process_time

# Algorithm 1 - Dictionaries
infile = open("PeterPan.txt", 'r')
largeText = infile.read()
infile.close()
words = largeText.split()
counter = 0

start = process_time()
for x in words:
    x = x.strip("\"\'()[]{},.?!<>:;-")
    if x in DICT: # Search the dictionary
        counter += 1
end = process_time()

print(counter)
print("Time elapsed with DICT (in seconds):",
      end - start)

# Algorithm 2 - LISTS
# using words from Algorithm 1

counter = 0
start = process_time()
for x in words:
    x = x.strip("\"\'()[]{},.?!<>:;-")
    if x in LIST: # Search through LIST
        counter += 1
end = process_time()
print(counter)
print("Time elapsed with LIST (in seconds):",
      end - start)
'''

# Dictionaries within Dictionaries!
'''
- We want to keep track of all students who are
enrolled in specific courses.
- schedule is a dictionary with the class name
mapping to another dictionary containing studentIDs
mapping to student namedtuples
'''

from collections import namedtuple

Student = namedtuple('Student', 'name id')

s1 = Student("Richert", 1234567)
s2 = Student("John Doe", 7654321)
s3 = Student("Jane Doe", 5555555)
s4 = Student("Mr. E", 1111111)
s5 = Student("Chris Gaucho", 2222222)

'''
- schedule is mapped by course keys to a dictionary
of students.
- inner-dictionary has student IDs mapped to
student namedtuples
'''
schedule = {'CS8':{}, 'CS16':{}, 'CS24':{}}

def print_schedule():
    ''' Prints the course schedule and all students enrolled
        - Iterate through key/value pairs using two variables
        - 1st variable is key, 2nd variable is value
    '''
    for course, students in schedule.items():
        print("{:6s}:\n\t".format(course), end="")
        for studentId, student in students.items():
            print("ID: {:7d}, Name: {}\n\t".format(
                studentId, student.name), end="")
        print()

#print_schedule()

def add_student(course, student):
    ''' Adds a student to a class '''
    enrolled_students = schedule.get(course)

    if enrolled_students == None:
        print("Course does not exist")
        return

    enrolled_students[student.id] = student

# Sanity check
#add_student('CS8', s2)
#add_student('CS8', s1)
#add_student('CS16', s3)
#print_schedule()

def add_course(course):
    if schedule.get(course) == None:
        schedule[course] = {}

def remove_course(course):
    schedule.pop(course)

def remove_student(course, student):
    enrolled_students = schedule.get(course)

    if enrolled_students == None:
        print(course, "does not exist")
        return
    enrolled_students.pop(student.id)

print('*' * 20)
print_schedule()
print('*' * 20)    
add_student('CS8', s1)
add_student('CS8', s2)
add_student('CS16', s3)
add_student('CS24', s4)
print_schedule()
print('*' * 20)

add_course("CS32")
add_student("CS32", s5)
print_schedule()
print('*' * 20)

remove_course('CS8')
print_schedule()
print('*' * 20)

add_course('CS8')
print_schedule()
print('*' * 20)

#remove_course("PSTAT120")  # Error, does not exist
#print_schedule()
#print('*' * 20)
```