# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 02:40:42 2021

@author: Jerome Penaflor
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def total_poly(x):
        sum = 0
        for i in range(len(L)):
            exp = (len(L)-1)-i
            sum += L[i]*(x**exp)
        return sum
    return total_poly