# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:16:52 2023

@author: Sourish Bhat
"""
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
print("Please choose one of the following operators: + , - , * , / , ^ , **")
c=input("Enter the operator:")

if (c== "+"):
    print("The sum of the numbers is:",a+b)
elif(c=="-"):
    print("The difference of the numbers is:",a-b)
elif(c=="*"):
    print("The multiplication of the numbers is:",a*b)
elif(c=="/"):
    print("The division of the numbers is:",a/b)
elif(c=="**"):
    print("The square root of the number is:",a**b)
else:
    print("Invalid Operator.")
