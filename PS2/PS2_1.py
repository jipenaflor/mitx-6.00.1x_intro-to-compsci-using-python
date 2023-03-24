# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:51:08 2021

@author: Jerome Penaflor
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for m in range(12):
    balance -= monthlyPaymentRate*balance
    balance += (annualInterestRate/12.0)*balance
print("Remaining balance: ", round(balance,2))