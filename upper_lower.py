


def letter_counter():
    upper_count=0
    lower_count=0
    string=input("Enter a string: ")
    for i in string:
        if i.isupper():
            upper_count+=1
        elif i.islower():
            lower_count+=1
    return upper_count,lower_count
upper_count,lower_count=letter_counter()
print(f"NO of upper case {upper_count}")
print(f"NO of lower case {lower_count}")
