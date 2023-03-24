# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:30:39 2021

@author: Jerome Penaflor
"""

s = 'gkayaixdnoux'

tmpA = ""
tmpB = ""

for i in range(len(s)-1):
    tmpA += s[i]
    k = i
    for j in range(k+1, len(s)):
        if s[k] <= s[j]:
            tmpA += s[j]
            k += 1
        else:
            break
    if len(tmpA) > len(tmpB):
        tmpB = tmpA
    tmpA = ""
print("Longest substring in alphabetical order is: "+ tmpB)