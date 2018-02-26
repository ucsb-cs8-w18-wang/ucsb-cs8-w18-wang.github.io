# lab06_tests.py

####################
from lab06 import totalWords

def test_totalWords1():
    assert totalWords("input1.txt") == 104

def test_totalWords2():
    assert totalWords("input2.txt") == 170

####################
from lab06 import longestWord

def test_longestWord1():
    assert longestWord("input1.txt") == "traditional"

def test_longestWord2():
    assert longestWord("input2.txt") == "responsible"

####################
from lab06 import charactersPerWord

def test_charactersPerWord1():
    assert charactersPerWord("input1.txt") == 4.278846153846154

def test_charactersPerWord2():
    assert charactersPerWord("input2.txt") == 4.3882352941176475


