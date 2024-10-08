'''
AUTHOR:Alex roy
Date: 08-10-2024
Python program to extract a word
'''
First_name=input("enter your First_name:")
Second_name=input("enter your Second_name;")
Full_name=First_name+" "+Second_name
print(Full_name)
length=len(First_name)
extract_First_name=Full_name[:length]
print(extract_First_name)