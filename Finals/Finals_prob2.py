# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 21:07:18 2021

@author: Jerome Penaflor
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    D1 = {}
    D2 = {}
    
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    elif len(L1) != len(L2):
        return False
    
    for x in L1:
        D1[x] = D1.get(x,0) + 1
        
    for y in L2:
        D2[y] = D2.get(y,0) + 1
    
    val1 = max(D1.values())
    val2 = max(D2.values())
    
    print(D1)
    print(D2)
    
    if val1 == val2:
        for key1, value1 in D1.items():
            for key2, value2 in D2.items():
                if val1 == value1 and val2 == value2:
                    if key1 == key2 and key1!= 0 and key2!=0:
                        return (key1, val1, type(key1))
                    else:
                        return False
    else:
        return False


print(is_list_permutation([0, 4, 8, 3, 0, 2, 2, 1, 4, 7, 8, 3, 7, 0, 0], [3, 4, 0, 3, 8, 0, 2, 0, 7, 2, 0, 3, 7, 2, 1])
)
    