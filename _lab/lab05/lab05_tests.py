#lab05_tests.py
from lab05 import create_screen

####################
from lab05 import invert_pixels

# Tests for invert_pixels
def test_invert_pixels1():
    assert invert_pixels([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) \
           == [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

def test_invert_pixels2():
    assert invert_pixels([[1, 0], [1, 0], [1, 0], [1, 0]]) \
           == [[0, 1], [0, 1], [0, 1], [0, 1]]

def test_invert_pixels3():
    assert invert_pixels([[0]]) \
           == [[1]]

def test_invert_pixels4():
    assert invert_pixels([[1, 1, 1], [0, 0, 0], [0, 0, 0]]) \
           == [[0, 0, 0], [1, 1, 1], [1, 1, 1]]

####################
from lab05 import fill_rect

# Tests for fill_rect
def test_fill_rect1():
    assert fill_rect(0,0,4,4,create_screen(5,5)) == \
           [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

def test_fill_rect2():
    assert fill_rect(1,1,3,2,create_screen(5,5)) == \
           [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0], [0, 0, 0, 0, 0]]

def test_fill_rect3():
    assert fill_rect(0,0,1,0,create_screen(3,3)) == \
           [[1, 0, 0], [1, 0, 0], [0, 0, 0]]

def test_fill_rect4():
    assert fill_rect(1,0,1,2,create_screen(3,3)) == \
           [[0, 0, 0], [1, 1, 1], [0, 0, 0]]

####################
from lab05 import draw_rect

def test_draw_rect1():
    assert draw_rect(0,0,4,4,create_screen(5,5)) == \
           [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

def test_draw_rect2():
    assert draw_rect(1,1,4,3,create_screen(5,5)) == \
           [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]

def test_draw_rect3():
    assert draw_rect(0,0,0,2,create_screen(3,3)) == \
           [[1, 1, 1], [0, 0, 0], [0, 0, 0]]

def test_draw_rect4():
    assert draw_rect(1,0,3,3,create_screen(4,4)) == \
           [[0, 0, 0, 0], [1, 1, 1, 1],
            [1, 0, 0, 1], [1, 1, 1, 1]]

####################
from lab05 import draw_line

def test_draw_line1():
    assert draw_line(0,0,4,4,create_screen(5,5)) == \
           [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

def test_draw_line2():
    assert draw_line(3,5,2,0,create_screen(6,6)) == \
            [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

def test_draw_line3():
    assert draw_line(1,1,1,4,create_screen(5,5)) == \
           [[0, 0, 0, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def test_draw_line4():
    assert draw_line(0,2,5,2,create_screen(6,6)) == \
           [[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]

def test_draw_line5():
    assert draw_line(2,2,2,2,create_screen(6,6)) == \
           [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
