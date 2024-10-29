'''
AUTHOR:Alex roy
Date: 28-10-2024
Python program to familiarize with for loop(n number).
'''
limit=int(input("Enter your limit:"))
for number in range(2,limit+1):
    isprime=True
    for i in range (2,(number//2)+1):
        if number%i==0:
            isprime=False
    if isprime:
        print(number)
