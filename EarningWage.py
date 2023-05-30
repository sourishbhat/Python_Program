# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:09:13 2023

@author: Sourish Bhat
"""
w=int(input("Enter your working hours in a week:"))
h=float(input("Enter your wage per hour:"))

e=w*h

if (e>5000):
    print("Your earning is greater than 5000.")
else: 
    print("Your earning is less than 5000.")