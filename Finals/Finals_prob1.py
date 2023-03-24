# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:58:08 2021

@author: Jerome Penaflor
"""

def sum_digits(s):
    total = 0
    for dig in s:
        if dig.isdigit():
            total += int(dig)
        else:
            if not any(char.isdigit() for char in s):
                raise ValueError
    return total

print(sum_digits("a;jk"))