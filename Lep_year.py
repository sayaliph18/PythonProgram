#Python Program to Check Leap Year
"""
#Method 1: Find Leap Year using  else-if Statements

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")

------------------------------------------------

#Method 2: Find Leap Year using Multiple else-if Statements

year = int(input("Enter year to be checked: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap year!")
        else:
            print("The year is not a leap year!")
    else:
        print("The year is a leap year!")
else:
    print("The year is not a leap year!")

------------------------------------------------------
"""
