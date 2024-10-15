'''
AUTHOR:Alex roy
Date: 15-10-2024
Python program to know the smallest of the three numbers
'''
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
if num1<num2 and num1<num3:
    print("Smallest number is:",num1)
elif num2<num1 and num2<num3:
    print("Smallest number is:",num2)
else:
    print("Smallest number is:", num3)