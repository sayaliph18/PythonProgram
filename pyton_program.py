"""
#Python Program to Print All Numbers in a Range Divisible by a Given Number

lower = int(input('Enter lower range : '))
upper = int(input('Enter upper range : '))
n = int(input('Enter the number to be divided by : '))
print('Given number divided by',n,':')
for i in range(lower,upper+1):
    if(i%n==0):
        print(i)

-----------------------------------------------------

#Sum of Digits Program in Python

n = int(input('Enter the number  : '))
total = 0
while(n > 0):
    dig = n % 10
    total = total + dig
    n = n // 10
print('Total sum of digits is : ',total)

----------------------------------------------------

#Sum of Digit of a Number using Recursion in Python

l = []
def sum_digits(b):
    if(b==0):
        return l
    dig = b % 10
    l.append(dig)
    sum_digits(b//10)
n = int(input('Enter the number: '))
sum_digits(n)
print("Sum of Digit of a Number: ",sum(l))

--------------------------------------------------
#Python Program to Count the Number of Digits in a Number

n = int(input('Enter number: '))
count = 0
while(n > 0):
    count = count + 1
    n = n//10
print('The number of digits in a number is ',count)

------------------------------------------------------
#Python Program to Find All the Divisors of an Integer

n = int(input('Enter number: '))
print('The divisors of the number are:')
for i in range(1,n+1):
    if(n%i==0):
        print(i)

------------------------------------------------------

#Python Program to Find the Smallest Divisor of an Integer

n = int(input('Enter an number: '))
a = []
for i in range(2,n+1):
    if (n%i==0):
        a.append(i)
a.sort()
print('Smallest divisor is:',a[0])

-----------------------------------------------

#Python Program to Print Binary Equivalent of an Integer using Recursion

l = []
def convert(b):
    if(b==0):
        return l
    dig = b % 2
    l.append(dig)
    convert(b//2)
a = int(input('Enter a number : '))
convert(a)
l.reverse()
print('Binary equivalent:')
for i in l:
    print (i)

------------------------------------------------

#Python Program to Print Binary Equivalent of a Number without Using Recursion

n = int(input('Enter a number : '))
a = []
while(n>0):
    dig=(n%2)
    a.append(dig)
    n = n//2
a.reverse()
print('Binary equivalent:')
for i in a:
    print (i)
"""

