'''
AUTHOR:Alex roy
Date: 15-10-2024
Python program to check whether the givem number is positive or not
'''
number=int(input("Enter a number:"))
if number>0:
    print("The given number",number," is positive")
elif number<0:
    print("The given number",number,"is negative")
else:
    print("the given number",number,"is zero")