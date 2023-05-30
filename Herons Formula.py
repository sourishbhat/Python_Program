# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 08:54:28 2023

@author: Sourish Bhat
"""
a=int(input("Enter the Side A:"))
b=int(input("Enter the Side B:"))
c=int(input("Enter the Side C:"))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**1/2

print("Area of the Triangle is:",area,"square cm")
