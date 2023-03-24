# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:03:14 2021

@author: Jerome Penaflor
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    score = 0
    SCRABBLE_LETTER_VALUES = {'a':1 , 'b':3, 'c':3, 'd':2,
        'e':1, 'f':4, 'g':2, 'h':4,'i':1, 'j':8, 'k':5,'l':1,
        'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,'s':1,'t':1,
        'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}
    
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n:
        score += 50
        
    return score

def test_getWordScore():
    """
    Unit test for getWordScore
    """
    failure=False
    # dictionary of words and scores
    words = {("", 7):0, ("it", 7):4, ("was", 7):18, ("scored", 7):54, ("waybill", 7):155, ("outgnaw", 7):127, ("fork", 7):44, ("fork", 4):94}
    for (word, n) in words.keys():
        score = getWordScore(word, n)
        if score != words[(word, n)]:
            print("FAILURE: test_getWordScore()")
            print("\tExpected", words[(word, n)], "points but got '" + str(score) + "' for word '" + word + "', n=" + str(n))
            failure=True
    if not failure:
        print("SUCCESS: test_getWordScore()")

test_getWordScore()