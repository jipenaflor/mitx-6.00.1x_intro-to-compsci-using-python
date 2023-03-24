# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:00:02 2021

@author: Jerome Penaflor
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    checker = ""
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                checker += i
                break
    print(checker)
    if checker == secretWord:
        return True
    else:
        return False

print(isWordGuessed('lettuce', ['z', 'x', 'q', 'l', 'e', 't', 't', 'u', 'c', 'e']))