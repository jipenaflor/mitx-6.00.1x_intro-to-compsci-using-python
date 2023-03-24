# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:47:08 2021

@author: Jerome Penaflor
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    newHand = hand.copy()
    for letter in word:
        newHand[letter] -= 1
    return newHand

def test_updateHand():
    """
    Unit test for updateHand
    """
    # test 1
    handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    handCopy = handOrig.copy()
    word = "quail"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'l':1, 'm':1}
    expectedHand2 = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function
    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function
        
    # test 2
    handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
    handCopy = handOrig.copy()
    word = "evil"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {'v':1, 'n':1, 'l':1}
    expectedHand2 = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)

        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    # test 3
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    hand2 = updateHand(handCopy, word)
    expectedHand1 = {}
    expectedHand2 = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
    if hand2 != expectedHand1 and hand2 != expectedHand2:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tReturned: ", hand2, "\n\t-- but expected:", expectedHand1, "or", expectedHand2)
        
        return # exit function

    if handCopy != handOrig:
        print("FAILURE: test_updateHand('"+ word +"', " + str(handOrig) + ")")
        print("\tOriginal hand was", handOrig)
        print("\tbut implementation of updateHand mutated the original hand!")
        print("\tNow the hand looks like this:", handCopy)
        
        return # exit function

    print("SUCCESS: test_updateHand()")

# end of test_updateHand

test_updateHand()