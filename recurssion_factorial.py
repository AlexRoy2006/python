'''
AUTHOR:Alex roy
Date: 03-12-2024
Program to find the factorial of a number using Recursion.
'''

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))