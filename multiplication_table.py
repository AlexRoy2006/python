'''
AUTHOR:Alex roy
Date: 28-10-2024
Python program to familiarize with for loop(Building a multiplication table ).
'''
num=int(input("Enter the number:"))
for i in range(1,13):
    ans=num*i
    print(f"{num}x{i}={ans}")