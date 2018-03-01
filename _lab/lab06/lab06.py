# lab06.py

from random import randrange

def rollDice():
    '''
    (10 points)
    Function that returns the sum of rolling two six-sided dice.
    - Note that the possible sum of rolling two dice is [2-12].
    However, this distribution is not uniform (i.e. rolling a 2 does
    not have the same probability as rolling a 6). Your function must
    use randrange correctly to account for this.
    '''
    return "stub"


def rollDistribution(n):
    '''
    (10 points)
    Function that rolls a pair of dice n number of times. Returns a
    list of ints, diceTally, that keeps track of the number of times
    a certain sum occurs.
    - Use the technique discussed in lecture where you can create a
    list of 13 integers, where the index of the list represents a
    particular dice roll value, and the value of that position represents
    the number of times that dice roll occurred.
    - Note: diceTally[0] and diceTally[1] will always be 0 since
    having rolling a pair of dice will never result in 0 or 1.
    - Your algorithm should call rollDice() n number of times when
    populating your list.
    '''
    return "stub"


def printDistribution(diceTally):
    '''
    (20 points)
    Function that prints the diceTally distribution in a specific
    format (see lab instructions for more details).
    - This function does not return anything since it is simply
    printing to the console.
    - Note: Your algorithm must iterate and print each dice roll value in
    a loop. Do not simply have 11 print statements for each dice roll value.
    - Be VERY PRECISE in your format. Each character matters for full credit.
    '''
    return


def totalWords(filename):
    '''
    (20 points)
    Reads the file with filename into your function and returns
    the number of words in the file.
    - Words are separated by whitespace characters, but does not include
    the following punctuation characters (,.!?;). You can assume contractions
    count as one word (i.e. "don't", "you'll", etc. are one word).
    - The split and strip functions may be useful in your implementation.
    - Your function should open the file for reading, and close
    the file before returning.
    '''
    return "stub"


def longestWord(filename):
    '''
    (20 points)
    Reads the file with filename into your function and returns
    the longest word in the text file.
    - Words are separated by whitespace characters, but does not include
    the following punctuation characters (,.!?;). You can assume contractions
    count as one word (i.e. "don't", "you'll", etc. are one word).
    - In the case of a tie, the 1st occurrence of the longest word
    is returned.
    - The split and strip functions may be useful.
    - Your function should open the file for reading, and close
    the file before returning.
    '''
    return "stub"


def charactersPerWord(filename):
    '''
    (20 points)
    Reads the file with filename into your function and returns
    the average number of characters per word.
    - Words are separated by whitespace characters, but does not include
    the following punctuation characters (,.!?;). You can assume contractions
    count as one word (i.e. "don't", "you'll", etc. are one word).
    - The split and strip functions may be useful.
    - Your function should open the file for reading, and close
    the file when done.
    '''
    return "stub"

