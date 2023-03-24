# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 02:55:42 2021

@author: Jerome Penaflor
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    newDict = {}
    for key, value in d.items():
        if value not in newDict:
            newDict[value] = [key]
        else:
            newDict[value].append(key)
            newDict[value].sort()
    
    return newDict

print(dict_invert({8: 6, 2: 6, 4: 6, 6: 6}))