'''
AUTHOR:Alex roy
Date: 15-10-2024
Python program to calculate the value after discount
'''
from multiprocessing.managers import Value

P_Amount=int(input("Enter your Purchase Amount:"))
if P_Amount>500:
    discount=P_Amount*20/100
    final_amount=P_Amount-discount
    print(final_amount)
elif P_Amount>=200 and P_Amount<=500:
    discount = P_Amount * 10 / 100
    final_amount = P_Amount - discount
    print(final_amount)
else:
    print(P_Amount)