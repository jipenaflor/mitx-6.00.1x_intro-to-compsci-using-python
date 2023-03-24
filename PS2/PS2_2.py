# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:04:17 2021

@author: Jerome Penaflor
"""

balance = 3926 #3329, 310 #4773, 440
annualInterestRate = 0.2

def checker(bal, payment, interest):
    for m in range(12):
        bal -= payment
        bal += (interest/12.0)*bal
    if bal <= 0:
        return payment
    else:
        return checker(balance, payment+10, interest)

minMonthlyPayment = checker(balance, 10, annualInterestRate)
print("Lowest Payment: ", minMonthlyPayment)