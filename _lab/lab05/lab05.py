# lab05.py

# lab05.py (solutions)

# From lecture - INCLUDE THiS FUNCTION IN YOUR SUBMISSION
def create_screen(rows, columns):
    '''
    Creates a screen of rows x columns pixels
    '''
    grid = []
    for x in range(rows):
        grid.append([0] * columns)
    return grid


# From lecture
def print_screen(screen):
    ''' Prints the screen to the console.
        When a pixel == 0, then a '*' is displayed
        When a pixel == 1, then a ' ' is displayed
    '''
    for x in range(len(screen)):
        for y in range(len(screen[0])):
            if screen[x][y] == 0:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    return


def invert_pixels(screen):
    '''
    (20 points)
    Changes all pixels from 0 to 1 or 1 to 0
    on the screen.
    - Returns the updated screen.
    '''
    return "stub"


def fill_rect(ulrow,ulcol,lrrow,lrcol,screen):
    '''
    (20 points)
    Draws (fills) a rectangle on the screen defined by
    the upper-left (ulrow,ulcol) and lower-right points
    (lrrow,lrcol) on the screen.
    - Returns the updated screen.
    - You may assume that these upper-left and lower-right
    points are the correct types (integers) and within the
    bounds of the screen dimensions.
    '''
    return "stub"


def draw_rect(ulrow,ulcol,lrrow,lrcol,screen):
    '''
    (20 points)
    Draws only the outline of a rectangle of the screen defined by
    the upper-left and lower-right points. It does not "fill"
    the rectangle.
    - Returns the updated screen.
    - You may assume that these upper-left and lower-right
    points are correct type (integers) and within the
    bounds of the screen dimensions.
    '''
    return "stub"


def draw_line(row1,col1,row2,col2,screen):
    '''
    (40 points)
    Draws a line between two points (row1,col1 is one point,
    (row2,col2 is the other point) on the screen.
    - Return the updated screen.
    - You may assume that these upper-left and lower-right
    points are correct type (integers) and within the bounds of the
    screen dimensions.
    '''
    return "stub"
         

# Testing your functionality visually by printing the screen
# should go in the if __name__=='__main__' condition.
# Recall that this code gets executed when executing the module directly.
# When lab05.py is imported, then this code will not execute.
if __name__=="__main__":
    print("Run visual print screen tests here")
    #screen = create_screen(20,20) # Creates a 20x20 screen
    #print_screen(screen)
    
