#Python Program to Check Whether a Number is Positive or Negative

n = int(input('Enter number : '))

if (n > 0):
    print(n, 'is a positive number')
elif (n == 0):
    print(n,'is neither positive nor negative number')
else:
    print(n,'is negative number')