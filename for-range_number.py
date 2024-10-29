'''
AUTHOR:Alex roy
Date: 28-10-2024
Python program to familiarize with for loop(With an input number).
'''
number=int(input("Enter a number:"))
isprime = True
for i in range(2,number//2+1):
    if number % i ==0:
        isprime=False
        break
if isprime:
    print(f"The given number {number} is prime")
else:
    print(f"The given number{number}is not prime")



