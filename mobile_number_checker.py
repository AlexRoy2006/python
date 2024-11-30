'''
AUTHOR:Alex roy
Date: 30-11-2024
Python program to know whether a mobile number is valid or not using function
'''

def number():
    mobile_number = input("Enter a mobile number:")
    if len(mobile_number)==10:
        if mobile_number[0]==9 or mobile_number[0]==8 or mobile_number[0]==7:
            print("It is a valid mobile number")
        else:
            print("It is not a valid mobile number")
    else:
        print("It is not a valid mobile number")

number()


