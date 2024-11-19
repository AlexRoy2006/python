list1=[]
list2=[]
list1_size=int(input("Enter the no of elments in list 1:"))
for num in range(list1_size):
    print("Enter the elements of list1:")
    list1.append(int(input()))
list2_size=int(input("Enter the no elements in list 2:"))
for num in range(list2_size):
    print("Enter the elements of list2:")
    list2.append(int(input()))
print(list1,list2)
combined_list=list1+list2
print(combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
even_list.sort()
odd_list.sort()
print(even_list)
print(odd_list)
combined_list=odd_list+even_list
print(combined_list)