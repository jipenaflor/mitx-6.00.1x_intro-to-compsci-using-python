# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:06:27 2021

@author: Jerome Penaflor
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    tmp = []
    ans = ""
    for i in range(len(secretWord)):
        tmp.append("_ ")
        
    for j in range(len(lettersGuessed)):
        for k in range(len(secretWord)):
            if lettersGuessed[j] == secretWord[k]:
                tmp[k] = lettersGuessed[j]
    
    for m in tmp:
        ans += m
        
    return ans


wordToGuess = 'apple' 
playerAttempt = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(wordToGuess, playerAttempt))