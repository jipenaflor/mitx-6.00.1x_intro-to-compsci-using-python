# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:47:36 2021

@author: Jerome Penaflor
"""

balance = 3926 #3329, 310 #4773, 440
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
lbound = balance/12
hbound = (balance*((1+monthlyInterestRate)**12))/12

def checker(bal, mInterest, low, high):
    mid = (low + high)/2
    payment = round(mid, 2)
    for m in range(12):
        bal -= payment
        bal += (mInterest)*bal
    if round(bal, 2) > 0.10:
        return checker(balance, mInterest, payment, high)
    elif round(bal, 2) < -0.10:
        return checker(balance, mInterest, low, payment)
    else:
        return payment

minMonthlyPayment = checker(balance, monthlyInterestRate, lbound, hbound)
print("Lowest Payment: ", minMonthlyPayment)