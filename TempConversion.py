# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:14:50 2023

@author: USER 5
"""

''' Get the temp. from the user either in Celsius or Fahrenheit. If the user input is Celsius
    Display in Fahrenheit and vice versa.  C=5/9*(F-32)'''
    
a=float(input("Enter the Temperature:"))
print("Please choose one of the Degrees: F or C")
b=input("Enter the degree:")

if(b=="F"):
    print("The temperature in Celsius is:", (5/9)*(a-32))