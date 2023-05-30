# -*- coding: utf-8 -*-
"""
Created on Tue May 23 10:58:34 2023

@author: USER 5
"""

'''WPP to find the multiples of a number accepted from a user from the 5 user inputed numbers'''

a=int(input("Enter the number:"))
b=int(input("Enter the first multiple:"))
c=int(input("Enter the second multiple:"))
d=int(input("Enter the third multiple:"))
e=int(input("Enter the fourth multiple:"))
f=int(input("Enter the fifth multiple:"))

if(b%a==0):
    print(b,"is a multiple of",a)
else:
    print(b,"is not a multiple of",a)

if(c%a==0):
    print(c,"is a multiple of",a)
else:
    print(c,"is not a multiple of",a)

if(d%a==0):
    print(d,"is a multiple of",a)
else:
    print(d,"is not a multiple of",a)

if(e%a==0):
    print(e,"is a multiple of",a)
else:
    print(e,"is not a multiple of",a)
    
if(f%a==0):
    print(f,"is a multiple of",a)
else:
    print(f,"is not a multiple of",a)