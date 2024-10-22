'''
AUTHOR:Alex roy
Date: 22-10-2024
Python program to calculate largest of three numbers
'''
temp=float(input("Enter temperature:"))
cf=input("Is this in (C)elsius or (F)arenheit")
if cf=="C":
    f=(9/5*temp)+32
    print(temp,"Celsius is",f,"Farenheit.")
else:
    c=5/9*(temp-32)
    print(temp,"Farenheit is",c,"Celsius.")

