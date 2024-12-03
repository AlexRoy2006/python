'''
AUTHOR:Alex roy
Date: 03-12-2024
Recursive function to multiply two positive numbers.
'''
def mul_numbers(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+mul_numbers(num1,num2-1)
print(mul_numbers(4,6))


