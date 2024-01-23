#Python Program to Check if a Number is Odd or Even

"""
#Method 1: (Using if-else and Modulus Operator)

n = int(input('Enter a number : '))

if n % 2 == 0:
    print(n ,'is even number')
else:
    print(n, 'is odd number')

--------------------------------------------------


#Method 2: (Using Bitwise Operator)

n = int(input('Enter a number : '))

if n & 1:
    print(n, 'is odd number')
else:
    print(n, 'is even number')

---------------------------------------------------

#Method 3: (Using Recursion)

def check(n):
    if (n < 2):
        return(n % 2 == 0)
    return (check(n-2))

n = int(input('Enter a number : '))

if (check(n) == True):
    print(n, 'is even number')
else:
    print(n, 'is odd number')

--------------------------------------------------

#Method 4: (Using Lambda Function)

check_number = lambda num: "even" if num % 2 == 0 else "odd"

n = int(input('Enter a number : '))

result = check_number(n)

print(n, 'is',result,'number')

-------------------------------------------------
"""


