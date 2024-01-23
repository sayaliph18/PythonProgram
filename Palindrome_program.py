# Palindrome Program in Python


###  Palindrome number in Python is a number that remains the same when its digits are reversed
"""
# Method 1: Palindrome Program in Python using While Loop

n = int(input('Enter number : '))

temp = n
rev = 0
while (n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

if (temp == rev):
    print('The number is a palindrome')
else:
    print('The number is not a palindrome')


-------------------------------------------------

#Method 2: Palindrome in Python using Built-in Function

def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))

n = int(input('Enter a number: '))

if is_palindrome(n):
    print('The number is a palindrome')
else:
    print('The number is not a palindrome')

--------------------------------------------------

#Method 3: Palindrome in Python using Slicing

def is_palindrome(n):
    num_str = str(n)
    reversed_str = num_str[::-1]
    return num_str == reversed_str


n = int(input("Enter a number:"))

if is_palindrome(n):
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome.")

----------------------------------------------------

# method 4 : Using if else condition

str = input("Enter a string: ")
if (str == str[::-1]):
    print('This is a palindrome')
else:
    print('This is not a palindrome')


---------------------------------------------------
#Method 5: Reverse a Number in Python using Recursion

def is_palindrome(n, temp, rev=0):
    if n == 0:
        if temp == rev:
            return "The number is a palindrome!"
        else:
            return "The number isn't a palindrome!"
    else:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
        return is_palindrome(n, temp, rev)


n = int(input("Enter number:"))
result = is_palindrome(n, n)
print(result)

------------------------------------------------------
"""



