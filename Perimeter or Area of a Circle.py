# -*- coding: utf-8 -*-
"""
Created on Tue May 23 11:00:35 2023

@author: USER 5
"""

'''WPP to display a menu for calculating area of a circle or perimeter of a circle.'''

# Starting of the program
print("Please choose one of the following options: 1. Perimeter of Circle; 2. Area of Circle")
a=int(input())
r=float(input("Enter the radius of the circle:"))

# Value of Pi
pi=3.14

# Formulae for perimeter and area of the circle respectively.
p=2*pi*r
ar=pi*r**2

# if conditions.
if(a==1):
    print("The perimeter of the circle is",p,"cm")
    
if(a==2):
    print("The area of the circle is",ar,"square cm")
    