# lab03_tests.py


from lab03 import notStringContainingR

# Tests for notStringContainingR
def test_notStringContainingR_1():
    assert notStringContainingR("word") == False

def test_notStringContainingR_2():
    assert notStringContainingR("super") == False

def test_notStringContainingR_3():
    assert notStringContainingR("ReEl") == False

def test_notStringContainingR_4():
    assert notStringContainingR("") == True

def test_notStringContainingR_5():
    assert notStringContainingR(3.14) == True

####################
from lab03 import hasVowel

# Tests for hasVowel
def test_hasVowel_1():
    assert hasVowel(True) == False

def test_hasVowel_2():
    assert hasVowel("Pythn") == False

def test_hasVowel_3():
    assert hasVowel("") == False

def test_hasVowel_4():
    assert hasVowel("borg") == True

def test_hasVowel_5():
    assert hasVowel("frEE") == True

####################
from lab03 import isNumber

# Tests for isNumber
def test_isNumber_1():
    assert isNumber("1") == False

def test_isNumber_2():
    assert isNumber(-1) == True

def test_isNumber_3():
    assert isNumber(True) == False

def test_isNumber_4():
    assert isNumber(3.14) == True

def test_isNumber_5():
    assert isNumber([0]) == False

####################
from lab03 import onlyContainsStrings

# Tests for onlyContainsStrings
def test_onlyContainsStrings_1():
    assert onlyContainsStrings([]) == False

def test_onlyContainsStrings_2():
    assert onlyContainsStrings(["a", "c", ""]) == True

def test_onlyContainsStrings_3():
    assert onlyContainsStrings(["18", 18, "eighteen"]) == False
    
def test_onlyContainsStrings_4():
    assert onlyContainsStrings([-1, "-1"]) == False

def test_onlyContainsStrings_5():
    assert onlyContainsStrings("python") == False

####################
from lab03 import contains

# Tests for contains
def test_contains_1():
    assert contains([], [4, [], 5]) == True

def test_contains_2():
    assert contains("18", [18, 18.0, "18"]) == True

def test_contains_3():
    assert contains("element", []) == False

def test_contains_4():
    assert contains("item", ("item")) == False

def test_contains_5():
    assert contains((1,2), [1, 2, "3", (1,2)]) == True
                    
####################
from lab03 import abbreviate

# Tests for abbreviate
def test_abbreviate_1():
    assert abbreviate("January") == "Jan"

def test_abbreviate_2():
    assert abbreviate(20) == ""

def test_abbreviate_3():
    assert abbreviate("At") == "At"

def test_abbreviate_4():
    assert abbreviate("T") == "T"

def test_abbreviate_5():
    assert abbreviate(["A", "T"]) == ""

####################
from lab03 import hasMultiplesOf

# Tests for hasMultiplesOf
def test_hasMultiplesOf_1():
    assert hasMultiplesOf(3, [-3, 0, 3, 6]) == True

def test_hasMultiplesOf_2():
    assert hasMultiplesOf("3", [-3, 0, 3, 6]) == False

def test_hasMultiplesOf_3():
    assert hasMultiplesOf(3, (-3, 0, 3, 6)) == False

def test_hasMultiplesOf_4():
    assert hasMultiplesOf(1.1, [1.1, 2.2, 4.4]) == True

def test_hasMultiplesOf_5():
    assert hasMultiplesOf(5, []) == False

####################
from lab03 import countEvens

# Tests for countEvens
def test_countEvens_1():
    assert countEvens([0,2,4]) == 3

def test_countEvens_2():
    assert countEvens([0,"2","Four", 6]) == 2

def test_countEvens_3():
    assert countEvens((0,2,4)) == 0

def test_countEvens_4():
    assert countEvens([-1,1,3,5,7]) == 0
    
def test_countEvens_5():
    assert countEvens([1.0,2.0,3.0,4.0,5.0,6.0,7.0,-2.0]) == 4

####################
from lab03 import computeGrade

# Tests for computeGrade
def test_computeGrade_1():
    assert computeGrade(90) == "A"

def test_computeGrade_2():
    assert computeGrade("80") == ""

def test_computeGrade_3():
    assert computeGrade(79.9) == "C"

def test_computeGrade_4():
    assert computeGrade(101) == ""

def test_computeGrade_5():
    assert computeGrade(-1) == ""

####################
from lab03 import expensiveBooks, Book

b1 = Book("Title1", "Author1", 5.99)
b2 = Book("Title2", "Author2", 0.99)
b3 = Book("Title3", "Author3", 20)
b4 = Book("Title4", "Author4", 0)
b5 = Book("Title5", "Author5", 100)
bookList = [b1,b2,b3,b4,b5]

# Tests for expensiveBooks
def test_expensiveBooks_1():
    assert expensiveBooks("0", bookList) == []

def test_expensiveBooks_2():
    assert expensiveBooks(5.99, bookList) == ['Title1','Title3','Title5']

def test_expensiveBooks_3():
    assert expensiveBooks(25, bookList) == ['Title5']

def test_expensiveBooks_4():
    assert expensiveBooks(5.99, (b1,b2)) == []

def test_expensiveBooks_5():
    assert expensiveBooks(101, bookList) == []

