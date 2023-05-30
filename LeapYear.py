'''Accept an year from the user and check whether it is a leap year or not.'''
a=int(input("Please enter the year:"))

if(a%4==0):
    print("The given year is a leap year.")
else:
    print("The given year is not a leap year.")
