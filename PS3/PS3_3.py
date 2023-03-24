# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:49:21 2021

@author: Jerome Penaflor
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    import string
    tmp = []
    availableLetters = ""
    
    for i in string.ascii_lowercase:
        tmp.append(i)

    for j in lettersGuessed:
        tmp.remove(j)
    
    for k in tmp:
        availableLetters += k
    return availableLetters
        

playerAttempt = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(playerAttempt))