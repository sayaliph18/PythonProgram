#Python Program to Reverse a Number

"""
#Method 1: Reverse a Number in Python using Slice Operator

n = int(input('Enter a number: '))
reversed_number = int(str(n)[::-1])
print('Reversed Number : ',reversed_number)

----------------------------------------------------------

#Method 2: Reverse a Number in Python using While Loop

n = int(input('Enter a number: '))
rev = 0
while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

print('Reverse of the number : ',rev)

---------------------------------------------------------

#Method 3: Reverse a Number in Python using Recursion

def reverse_number(number):
    if number < 10:
        return number
    else:
        last_digit = number % 10
        remaining_number = number // 10
        reversed_number = reverse_number(remaining_number)
        return int(str(last_digit) + str(reversed_number))

number = int(input('Enter a number : '))
reverse_number = reverse_number(number)
print('Reversed number :  ',reverse_number)

-------------------------------------------------------
"""

