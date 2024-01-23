#Python Program to Print Integers that isn’t Divisible by Either 2 or 3

"""
#Method1 : Using if-else condition

num = int(input("Enter a number : "))
if(num % 2 != 0) and (num % 3 != 0):
    print(num,'is not divisible by 2 or 3')
else:
    print(num, 'is divisible by 2 or 3')

--------------------------------------------------

#Method1 : Using for loop


print('All integers that aren’t divisible by either 2 or 3 ')
for i in range(0,51):
    if(i % 2 != 0) and (i % 3 != 0):
        print(i)

----------------------------------------------------
"""
