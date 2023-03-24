# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:47:59 2021

@author: Jerome Penaflor
"""

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    
    elem = []
    
    def findElem(j):
        for k in j:
            if type(k) == int:
                elem.append(k)
            else:
                findElem(k)
        
    for i in t:
        if type(i) == int:
            elem.append(i)
        else:
            findElem(i)
    
    return max(elem)

print(max_val((5, (1,2), [[1],[2]])))

