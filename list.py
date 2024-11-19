list=[1,2,2,3,3,4,5,6]
unique_list=[]
for num in list:
    if num not in unique_list:
        unique_list.append(num)
print("The original list is :",list)
print(list)
