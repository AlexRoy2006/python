'''
AUTHOR:Alex roy
Date: 30-11-2024
Python program to know whether a triangle is a Right Triangle or not.
'''
def is_right_triangle(side1,side,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False
side1=int(input("Enter the side 1 of the triangle:"))
side2=int(input("Enter the side 2 of the triangle:"))
side3=int(input("Enter the side 3 of the triangle:"))
if is_right_triangle(side1,side2,side3):
    print("It is a right angled trangle")
else:
    print("It is not a right anbled triangle")