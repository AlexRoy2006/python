'''
AUTHOR:Alex roy
Date: 15-10-2024
Python program to know the sum of digits
'''
num=int(input("Enter a number:"))
sum=0
while num>0:
    r=num%10
    sum=sum+r
    num=num//10
print(sum)