# lab04_tests.py

from lab04 import totalCharacters

# Tests for totalCharacters
def test_totalCharacters_1():
    assert totalCharacters(["this", "is", "a", "list"]) == 11

def test_totalCharacters_2():
    assert totalCharacters(["this", "is", "a", 2, "list"]) == -1

def test_totalCharacters_3():
    assert totalCharacters([]) == 0

def test_totalCharacters_4():
    assert totalCharacters("1,2,3") == -1

def test_totalCharacters_5():
    assert totalCharacters([1,"2","3"]) == -1

####################
from lab04 import factorial

# Tests for factorial
def test_factorial_1():
    assert factorial(4) == 24

def test_factorial_2():
    assert factorial(4.2) == -1

def test_factorial_3():
    assert factorial("4") == -1

def test_factorial_4():
    assert factorial(0) == 1

def test_factorial_5():
    assert factorial(-2) == -1

####################
from lab04 import maxNum
def test_maxNum_1():
    assert maxNum([]) == None

def test_maxNum_2():
    assert maxNum([4,3,12,2]) == 12

def test_maxNum_3():
    assert maxNum([-1.1,-1.2,-3.3,-2.2]) == -1.1

def test_maxNum_4():
    assert maxNum("1,2,3") == None

def test_maxNum_5():
    assert maxNum([4,4,"4",3]) == None

####################
from lab04 import indexOf

# Tests for indexOf
def test_indexOf_1():
    assert indexOf("tree", [4, "x", "tree", -1.2]) == 2

def test_indexOf_2():
    assert indexOf(3, ["1", "2", "3"]) == None

def test_indexOf_3():
    assert indexOf(3, []) == None

def test_indexOf_4():
    assert indexOf(1, [3, 1, 1, 2]) == 1

def test_indexOf_5():
    assert indexOf(1, "1") == None

####################
from lab04 import Item

i1 = Item('Eggs', 2.00, 2)
i2 = Item('Milk', 4.00, 0)
i3 = Item('Honey', 3.00, 3)
i4 = Item('Orange', 1.00, 0)

from lab04 import unpopularItems

# Tests for unpopularItems
def test_unpopularItems_1():
    assert unpopularItems([i1, i3]) == []

def test_unpopularItems_2():
    assert unpopularItems([i1, i2]) == [i2]

def test_unpopularItems_3():
    assert unpopularItems([i4, i3, i2, i1]) == [i4, i2]

def test_unpopularItems_4():
    assert unpopularItems([i2, i4]) == [i2, i4]

def test_unpopularItems_5():
    assert unpopularItems([]) == []

####################
from lab04 import updatePrice
def test_updatePrice_1():
    assert updatePrice(100, [i1, i2]) == [Item('Eggs', 4.00, 2),
                                          Item('Milk', 8.00, 0)]

def test_updatePrice_2():
    assert updatePrice(50, [i3, i4]) == [Item('Honey', 4.50, 3),
                                         Item('Orange', 1.50, 0)]

def test_updatePrice_3():
    assert updatePrice(0, [i1, i3]) == [Item('Eggs', 2.00, 2),
                                       Item('Honey', 3.00, 3)]

def test_updatePrice_4():
    assert updatePrice(-50, [i2, i4]) == [Item('Milk', 2.00, 0),
                                          Item('Orange', 0.50, 0)]

def test_updatePrice_5():
    assert updatePrice(-100, [i1, i2, i3, i4]) == [Item('Eggs', 0.00, 2),
                                                   Item('Milk', 0.00, 0),
                                                   Item('Honey', 0.00, 3),
                                                   Item('Orange', 0.00, 0)]
