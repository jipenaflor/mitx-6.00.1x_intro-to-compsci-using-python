# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:01:54 2021

@author: Jerome Penaflor
"""

def isMyNumber(secretNum):
    if secretNum == 5:
        return 0
    elif secretNum < 5:
        return -1
    else:
        return 1
        
def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    else:
        foundNumber = False
        while not foundNumber:
            sign = isMyNumber(guess)
            if sign == -1:
                guess += 1
            elif sign == 1:
                guess -= 1
            else:
                foundNumber = True
    return guess

print(jumpAndBackpedal(isMyNumber))