'''
AUTHOR:Alex roy
Date: 05-10-2024
Python program to get import math
'''
import math
from token import NUMBER

number=int(input("Enter a number:"))
sqrt=math.sqrt(number)
factor=math.factorial(number)
exp=math.exp(number)
print("Square root of",number,":",sqrt,)
print("Factorial of",number,":",factor,)
print(number," raised to 2:",exp,)